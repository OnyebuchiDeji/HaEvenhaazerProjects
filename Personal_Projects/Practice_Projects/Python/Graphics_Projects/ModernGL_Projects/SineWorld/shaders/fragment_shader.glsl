#version 330 core


//  Fragment shader determines the colour of each pixel on screen


/*  DC ==> Doesn't Change   */


layout(location=0) out vec4 fragColor;

uniform vec2 u_resolution;
uniform float u_time;

const float EPSILON = 0.001;
const float MAX_DIST = 1000.0;
const float STEPS = 300.0;
const float PI = acos(-1.0);
const int NUM_OCTAVES = 4;


float noise(vec2 p)
{
    //  This sin function is applied to each coordinate
    return sin(p[0]) + sin(p[1]);
}

mat2 rot(float a)
{
    float sa = sin(a);
    float ca = cos(a);
    return  mat2(ca, -sa, sa, ca);  //  2D rotation;
}

//  Fractional Brownian Motion function
float fbm(vec2 p)
{
    float res = 0.0;
    float amp = 0.5;
    float freq = 1.95;
    //  Summing up into res the effects of noise gotten by the number of given octaves...
    //  Using the principle of super position of waves.
    for (int i = 0; i < NUM_OCTAVES; i++){
        res += amp * noise(p); // Summing up noise
        //  Amplitude reduced
        amp *= 0.5;
        //  Frequency increased at each octave
        p = p * freq * rot(PI / 4.0) - res * 0.4;
    }

    return res;
}

//  Smooth water
float getWater(vec3 p)
{
    float d = p.y + 5.0 * sin(u_time) + 80.0;
    return d;
}

//  Wavy water
float getWavyWater(vec3 p)
{
    float d = p.y + 5.0 * sin(u_time) + 80.0;
    d += 6.0 * noise(p.xz * 0.02 + 1.0 * u_time);
    return d;
}

/*
    //  This gave a flat plain
    float getTerrainOG(vec3 p)
    {
        float d = 0;
        d += p.y + 2.0;
        return d;
    }
*/

//   Function to find distance to horizontal plain
float getTerrain(vec3 p)
{
    float d = 0;
    //  Because the plane is in the xz coordinates...
    //  Manipulations are on xz...
    //d += noise(p.xz); //  normal hills

    d -= 130.0 * noise(p.xz * 0.002);

    //  Changing amplitude(80.0) and frequency(0.01) of noise function
    d += 80.0 * noise(p.xz * 0.01) + 80.0;  //  Higher and more spaced hills

    //  Applying fbm
    d += 20.0 * fbm(p.xz * 0.1) * noise(p.xz * 0.01) + 20.0;

    d -= 2.0 * sin(0.6 * d);

    //  Shift down by 2 units
    d += p.y + 1.0;

    return d * 0.1;
}

/*
    //  Made a sphere
    float mapOG(vec3 p)
    {
        float d = 0.0;
        d += length(p) - 0.5;
        return d;
    }
*/

/*
//  Produced terrain with wavy water
float map(vec3 p)
{
    float d = 0.0;
    d += getTerrain(p);
    
    return min(d, getWavyWater(p));
}
*/

float map(vec3 p)
{
    float d = 0.0;
    d += getTerrain(p);
    
    return min(d, getWavyWater(p) + d); //  Produces detailed water
}

//  DC
float rayMarch(vec3 ro, vec3 rd)
{
    float dist = 0.0;
    for (int i = 0; i < STEPS; i++)
    {
        vec3 p = ro + dist * rd;
        float hit = map(p);
        if (abs(hit) < EPSILON) break;
        dist += hit;
        if (dist > MAX_DIST) break;
    }

    return dist;
}

//  DC
vec3 getNormal(vec3 p)
{
    vec2 e = vec2(EPSILON, 0.0);
    vec3 n = vec3(map(p)) - vec3(map(p - e.xyy), map(p - e.yxy), map(p - e.yyx));

    return normalize(n);
}

vec3 g_lightPos = vec3(250.0, 100.0, -300.0);

//  DC
vec3 getLight(vec3 p, vec3 rd)
{
    vec3 color = vec3(1);
    vec3 l = normalize(g_lightPos - p);
    vec3 normal = getNormal(p);
    vec3 v = -rd;
    vec3 r = reflect(-l, normal);

    float diff = 0.85 * max(dot(l, normal), 0.0);
    float specular = 0.4 * pow(clamp(dot(r, v), 0.0, 1.0), 10.0);
    float ambient = 0.2;

    return (ambient + specular + diff) * color;
}

//  DC
mat3 getCam(vec3 ro, vec3 lookAt)
{
    vec3 camF = normalize(vec3(lookAt - ro));
    vec3 camR = normalize(cross(vec3(0, 1, 0), camF));
    vec3 camU = cross(camF, camR);

    return mat3(camR, camU, camF);
}

vec3 getSky(vec3 p, vec3 rd)
{
    vec3 col = vec3(0.0);
    float sun = 0.01 / (1.0 - dot(rd, normalize(g_lightPos)));
    col = mix(col, vec3(0.3), 2.0 * fbm(vec2(20.0 * length(rd.xz), rd.y)));
    col += sun * 0.1;

    return col;
}

float getSoftShadow(vec3 p, vec3 lightPos)
{
    float res = 1.0;
    float dist = 0.01;
    float lightSize = 0.03;
    for (int i = 0; i < 8; i++)
    {
        float hit = map(p + lightPos * dist);
        res = min(res, hit / (dist * lightSize));
        if (hit < EPSILON) break;
        dist += hit;
        if (dist > 30.0) break;
    }

    return clamp(res, 0.0, 1.0);
}

float getAmbientOcclusion(vec3 p, vec3 normal)
{
    float occ = 0.0;
    float weight = 0.4;
    for (int i = 0; i < 8; i++)
    {
        float len = 0.01 + 0.02 * float(i * i);
        float dist = map(p + normal * len);
        occ += (len - dist) * weight;
        weight *= 0.85;
    }

    return 1.0 - clamp(0.6 * occ, 0.0, 1.0);
}

/*
    vec3 renderOG(vec2 uv)
    {
        vec3 col = vec3(0.0);
        vec3 ro = vec3(0.0, 1.0, -3.0);
        vec3 lookAt = vec3(0, 0, 0);
        vec3 rd = getCam(ro, lookAt) * normalize(vec3(uv, 2.0));

        float dist = rayMarch(ro, rd);
        vec3 p = ro + dist * rd;

        if (dist < MAX_DIST){
            col += getLight(p, rd);
        }
        return col;
    }
*/
vec3 render(vec2 uv)
{
    vec3 col = vec3(0.0);
    //  Causes camera motion
    vec3 ro = vec3(220.0, 50.0, 220.0);
    ro.xz *= rot(7.0 * 0.1 * sin(u_time * 0.5) + 1.5);  
    vec3 lookAt = vec3(0, 1, 0);
    //  Camera motion causing lines end here

    vec3 rd = getCam(ro, lookAt) * normalize(vec3(uv, 2.0));
    

    float dist = rayMarch(ro, rd);
    vec3 p = ro + dist * rd;
    	
    //col = mix(getSky(p, rd), col, exp(-0.0000007 * dist * dist));   //  Just fog

    col = mix(getSky(p, rd) * getSoftShadow(p, g_lightPos) * getAmbientOcclusion(p, getNormal(p)), col,
         exp(-0.0000007 * dist * dist));

    if (dist < MAX_DIST){
        col += getLight(p, rd);
    }

    return col;
}



void main()
{
    vec2 uv = (2.0 * gl_FragCoord.xy - u_resolution.xy) / u_resolution.y;
    vec3 color = render(uv);

    fragColor = vec4(pow(color, vec3(2.2)), 1.0);
}