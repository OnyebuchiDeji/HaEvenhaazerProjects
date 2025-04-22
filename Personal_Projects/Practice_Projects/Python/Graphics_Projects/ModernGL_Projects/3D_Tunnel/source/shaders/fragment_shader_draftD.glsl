#version 330 core

out vec4 fragColor;

in vec2 textureCoords;

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
    /*  Doing gl_FragCoord.xy / u_resilution.xy (which is the screen's resolution)...
      normalizes the window coordinates of the glsl window to be from...
      (0, 0) in bottom left to (1, 1) in top right
    */
    // vec2 normalizedCoords = (gl_FragCoord.xy / u_resolution.xy);
    /*  Now, subtracting half of the screen resolution from the coordinate origin...
        causes the origin to start at the center
    */
    /*
        Doing gl_FragCoord.xy - (0.5 * u_resolution) moves the screen 2d world coordinate origin to the center.
        Then, dividing by the u_resolution.y alone is to normalize the coordinates to be between 0 and 1 while...
        maintaining its aspect ratio: 16:9.
        If I was to divide by u_resolution.xy, the aspect ratio will be different, and this will cause the origin,
        gl_FragCoord.xy to move a little to the right
    */
    vec2 uv = (gl_FragCoord.xy - (0.5 * u_resolution)) / u_resolution.y;

    vec3 col = vec3(0.0);

    // float phi = atan(uv.y, uv.x);
    // float rho = length(uv.xy);
    // vec2 st = vec2(phi / (2 * PI + 0.5), 0.25/rho);
    // vec3 texture = texture(u_image_texture, uv).rgb;
    

    // col += texture;
    

    // col = clamp(col, 0.0, 1.0);

    fragColor = vec4(uv, 0, 1.0);

}
