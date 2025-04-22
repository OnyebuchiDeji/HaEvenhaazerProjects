#version 330 core

// layout(location=0) out vec4 fragColor;

out vec4 fragColor;

// in vec2 fragmentCoords;

uniform vec2 u_resolution;
uniform float u_time;

vec2 EG1()
{
    //  Multiplying by two to make the normalized coourdinate range to be from...
    //  0 -> 2 and the -1.0, causes the interval to be from -1 -> 1
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    vec4 color = vec4(normalizedCoord, 0, 1);
    return color;
}
vec2 EG2()
{
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    vec4 color = vec4(vec3(length(normalizedCoord)), 1);
    return color;
}
vec2 EG3()
{
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    normalizedCoord = abs(normalizedCoord);
    normalizedCoord -= 0.5;
    vec4 color = vec4(vec3(length(normalizedCoord)), 1);
    return color;
}
vec2 EG4()
{
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    normalizedCoord = abs(normalizedCoord);
    normalizedCoord -= 0.5;
    normalizedCoord *= 1.1;
    vec4 color = vec4(vec3(length(normalizedCoord)), 1);

    return color;
}
vec2 TheFractal()
{
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 32.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.1;
        normalizedCoord *= mat2(
            cos(0.2), -sin(0.2),
            sin(0.2), cos(0.2)
        );
    }
    vec4 color = vec4(vec3(length(normalizedCoord)), 1);

    return color;
}
vec2 MovingFractal()
{
    float angle = u_time * 0.5;
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 32.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.1;
        normalizedCoord *= mat2(
            cos(angle), -sin(angle),
            sin(angle), cos(angle)
        );
    }
    vec4 color = vec4(vec3(length(normalizedCoord)), 1);

    return color;
}
vec2 ColouredMovingFractal()
{
    float angle = u_time * 0.5;
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 32.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.1;
        normalizedCoord *= mat2(
            cos(angle), -sin(angle),
            sin(angle), cos(angle)
        );
    }
    vec4 color = vec4(length(normalizedCoord),
    length(normalizedCoord+vec2(0.2, -0.3)),
    length(normalizedCoord+vec2(-0.4, -0.1)), 1.0);

    return color;
}

float rand(vec2 co){
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

vec2 CustomFractal1()
{
    float angle = u_time * 0.03;
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 32.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.03;
        normalizedCoord *= mat2(
            cos(angle), -sin(angle),
            sin(angle), cos(angle)
        );
    }
    vec4 color = vec4(length(normalizedCoord+rand(vec2(0.1, 0.7))),
    length(normalizedCoord+vec2(0.1, -0.5)),
    length(normalizedCoord+vec2(-0.1, -0.15)), 1.0);

    return color;
}
vec2 CustomFractal2()
{
    float angle = u_time * 0.03;
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 120.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.03;
        normalizedCoord *= mat2(
            cos(angle), -sin(angle),
            sin(angle), cos(angle)
        );
    }
    vec4 color = vec4(length(normalizedCoord+rand(vec2(0.1, 0.7))),
    length(normalizedCoord+vec2(0.1, -0.5)),
    length(normalizedCoord+vec2(-0.1, -0.15)), 1.0);

    return color;
}



void main()
{   
    float angle = u_time * 0.03;
    vec2 normalizedCoord = gl_FragCoord.xy / u_resolution.xy * 2.0 - 1.0;
    for (float i = 0.0; i < 32.0; i+= 1.0)
    {
        normalizedCoord = abs(normalizedCoord);
        normalizedCoord -= 0.5;
        normalizedCoord *= 1.03;
        normalizedCoord *= mat2(
            cos(angle), -sin(angle),
            sin(angle), cos(angle)
        );
    }
    fragColor = vec4(length(normalizedCoord+rand(vec2(0.1, 0.7))),
    length(normalizedCoord+vec2(0.1, -0.5)),
    length(normalizedCoord+vec2(-0.1, -0.15)), 1.0);
}