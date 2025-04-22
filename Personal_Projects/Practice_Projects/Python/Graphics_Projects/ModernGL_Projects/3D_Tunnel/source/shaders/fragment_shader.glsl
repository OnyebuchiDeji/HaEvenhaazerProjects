#version 330 core

out vec4 fragColor;

in vec2 textureCoords;

/*
    DOn't need resolution to render
*/
uniform vec2 u_resolution;
uniform float u_time;

uniform sampler2D u_image_texture;
uniform vec2 u_texture_size;


const float PI = acos(-1.0);

// vec3 dynamic_color_grad()
// {
//     //  Normalized Pixel Coordinate (from 0 to 1)
//     vec2 uv = (gl_FragCoord.xy / u_resolution.xy);

//     //  Time varying pixel Color
//     vec3 col = 0.5 + 0.5 * cos((u_time + uv.xyx) + vec3(0, 2, 4));

//     return col;
// }

void renderNormalTexture()
{

    vec3 col = vec3(0.0);

    vec3 texture = vec3(texture(u_image_texture, textureCoords)).rgb;

    col += texture;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderNormalTexture2()
{
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;
    vec3 col = vec3(0.0);

    vec3 texture = vec3(texture(u_image_texture, textureCoords)).rgb;

    col += texture;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderTextureLightShow()
{
    // vec2 uv = (gl_FragCoord.xy / u_resolution.xy);
    vec2 uv = (gl_FragCoord.xy - (0.5 * textureCoords)) / textureCoords.y;

    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(uv.y, uv.x);
    float rho = length(uv.xy);

    vec2 st = vec2(phi / PI * 2, 0.25/rho);
    // st.x += u_time / 14;
    st.y += u_time / 2;
    // vec2 texts= textureCoords;
    

    vec3 texture = vec3(texture(u_image_texture, st )).rgb;


    col += texture;
    
    // col *= rho + 0.2;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderTextureTunnelCoolade1()
{
    // vec2 uv = (gl_FragCoord.xy / u_resolution.xy);
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;
    
    vec2 samplePos = uv*textureCoords;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(samplePos.y, samplePos.x);
    float rho = length(samplePos.xy);

    vec2 st = vec2(phi / PI * 2, 0.25/rho);
    st.x += u_time / 14;
    // st.y += u_time / 2;
    // vec2 texts= textureCoords;
    

    vec3 texture = vec3(texture(u_image_texture, st )).rgb;


    col += texture;
    
    // col *= rho + 0.2;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderTextureTunnelCoolade2()
{
    // vec2 uv = (gl_FragCoord.xy / u_resolution.xy);
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;
    // vec2 samplePos = (textureCoords.xy -(0.5*u_resolution))/ textureCoords.y;
    // vec2 samplePos = uv*textureCoords;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(uv.y, uv.x);
    float rho = length(uv.xy);

    vec2 st = vec2(phi / PI * 2, 0.25/rho);
    st.x += u_time / 14;
    // st.y += u_time / 2;
    // vec2 texts= textureCoords;
    

    vec3 texture = vec3(texture(u_image_texture, st*textureCoords )).rgb;

    col += texture;
    
    // col *= rho + 0.2;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderTextureTunnelCoolade3()
{
    vec2 uv = (gl_FragCoord.xy / u_resolution.xy);
    // // vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;
    // // vec2 samplePos = (textureCoords.xy -(0.5*u_resolution))/ textureCoords.y;
    vec2 samplePos = uv*textureCoords;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(samplePos.y, samplePos.x);
    float rho = length(samplePos.xy);

    vec2 st = vec2(phi / PI * 2, 0.25/rho);
    // st.x += u_time / 14;
    // st.y += u_time / 2;
    

    vec3 texture = vec3(texture(u_image_texture, st )).rgb;


    col += texture;
    
    //  Just adds shadow!
    col *= rho + 0.2;

    col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}

void renderTextureTunnelDark()
{
    /*
      This is the part that transposes the image's render origin to the screens center...
      because, remember, the tecxture coordinates where clamped to be betweeon 0 and 1...
      for those s and t values as I learned in the pyOpengl from GetIntoGameDev
    
    */
    vec2 samplePos = (textureCoords.xy) - 0.5;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(samplePos.y, samplePos.x);
    float rho = length(samplePos.xy);

    vec2 st = vec2(phi / PI, 0.25/rho);
    st.x += u_time / 14;
    st.y += u_time / 2;
    

    vec3 texture = vec3(texture(u_image_texture, st )).rgb;


    col += texture;
    
    //  Just adds shadow!
    col *= rho + 0.1;
    // col += phi;

    // col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}
void renderTextureTunnelLight2()
{
    /*
      This is the part that transposes the image's render origin to the screens center...
      because, remember, the tecxture coordinates where clamped to be betweeon 0 and 1...
      for those s and t values as I learned in the pyOpengl from GetIntoGameDev
    
    */
    vec2 samplePos = (textureCoords.xy) - 0.5;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(samplePos.y, samplePos.x);
    float rho = length(samplePos.xy);

    vec2 st = vec2(phi / PI * 0.5, 0.25/rho);
    st.x += u_time / 14;
    st.y += u_time / 2;
    

    vec3 texture = vec3(texture(u_image_texture, st)).rgb;


    col += texture * 0.05;
    
    //  Just adds shadow!
    col += 0.1 / rho * vec3(0.1, 0.1, 0.4);

    // col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}
void renderTextureTunnelLight()
{
    /*
      This is the part that transposes the image's render origin to the screens center...
      because, remember, the tecxture coordinates where clamped to be betweeon 0 and 1...
      for those s and t values as I learned in the pyOpengl from GetIntoGameDev
    
    */
    vec2 samplePos = (textureCoords.xy) - 0.5;
    vec3 col = vec3(0.0);

    //   Polar Coords

    float phi = atan(samplePos.y, samplePos.x);
    float rho = length(samplePos.xy);

    vec2 st = vec2(phi / PI * 0.5, 0.25/rho);
    st.x += u_time / 14;
    st.y += u_time / 2;
    
    /*
        The Line at the center is caused by the texture vec3in the line below.
        It is how the texture is mapped to the surface that has been warped, namely, st
        So to remove the line, st has to be modified!
    */

    vec3 texture = vec3(texture(u_image_texture, st)).rgb;


    col += texture;
    
    //  Just adds light at tunnel's end!
    col += 0.1 / rho * vec3(0.1, 0.1, 0.4);

    //  This legit darkens everything
    // col *= vec3(0.1, 0.1, 0.4);

    // col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);
}


void main()
{
    renderTextureTunnelLight();
}
