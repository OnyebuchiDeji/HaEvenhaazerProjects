#version 330 core

out vec4 fragColor;

uniform vec2 u_resolution;
uniform float u_time;



void main()
{
    //  Normalized Pixel Coordinate (from 0 to 1)
    vec2 uv = (gl_FragCoord.xy / u_resolution.xy);

    //  Time varying pixel Color
    vec3 col = 0.5 + 0.5 * cos((u_time + uv.xyx) + vec3(0, 2, 4));

    //  Output to Screen
    fragColor = vec4(col, 1.0);
    

}
