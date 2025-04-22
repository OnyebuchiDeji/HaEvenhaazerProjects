#version 330 core

out vec4 fragColor;

in vec2 textureCoords;

uniform vec2 u_resolution;
uniform float u_time;

uniform sampler2D u_image_texture;
uniform vec2 u_texture_size;

/*  
    In this file, the change is in the formula for st
*/

const float PI = acos(-1.0);

// vec3 dynamic_color_grad()
// {
//     //  Normalized Pixel Coordinate (from 0 to 1)
//     vec2 uv = (gl_FragCoord.xy / u_resolution.xy);

//     //  Time varying pixel Color
//     vec3 col = 0.5 + 0.5 * cos((u_time + uv.xyx) + vec3(0, 2, 4));

//     return col;
// }



void main()
{
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;

    vec3 col = vec3(0.0);

    float phi = atan(uv.y, uv.x);
    float rho = length(uv.xy);
    vec2 st = vec2(phi / (2 * PI + 0.5), 0.25/rho);
    vec3 texture = texture(u_image_texture, textureCoords * st).rgb;
    

    col += texture;
    

    // col = clamp(col, 0.0, 1.0);

    fragColor = vec4(col, 1.0);

}
