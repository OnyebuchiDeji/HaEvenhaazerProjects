#version 330 core

out vec4 fragColor;

in vec2 textureCoords;

uniform vec2 u_resolution;
uniform float u_time;

// uniform sampler2D u_image_texture;
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

// vec3 tunnel_render()
// {

//     vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;

//     vec3 col = vec3(0.0);

//     //   Polar Coords
//     float phi = atan(uv.y, uv.x);
//     float rho = length(uv);

//     vec2 st = vec2(phi / PI * 2, 0.25 / rho);
//     st.y += u_time / 2;
//     col +=  (st, 1.0) * u_texture_size;

//     col *= rho + 0.1;

//     col = clamp(col, 0.0, 1.0);
//     vec3 final = col * (texture(u_image_texture, u_resolution).rgb);
//     return final;
// }

void main()
{
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;
    // vec3 color = texture(u_image_texture, uv).rgb;

    vec3 col = vec3(0.0);

    float phi = atan(uv.y, uv.x);
    float rho = length(uv);

    col += vec3(phi / (2 * PI) + 0.5);

    /*  
        Initially, col = vec3(0.0) -> black.
        But when calculating the color of the pixel using phi...
        it is possible for this to happen:
        col = vec3(-0.5, 0.3, 1.5).
        But it is essential that all color components be between 0 and 1
        so the clamp function is used.
        So vec3(-0.5, 0.3, 1.5) -> vec3(0.0, 0.3, 1)
        Though, even without using the clamp function explicitely...
        the glsl shader program clamps it automatically
    */
    col = clamp(col, 0.0, 1.0);

    /*
        This time, when run, the white parts represents how the...
        value phi, because now it is divided by 2*PI, the gradient of tint is in a circular form
    */
    fragColor = vec4(col, 1.0);

}
