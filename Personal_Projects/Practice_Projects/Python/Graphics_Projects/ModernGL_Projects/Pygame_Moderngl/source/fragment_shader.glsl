#version 330 core


out vec4 fragColor;

in vec2 textureCoord;

uniform sampler2D textureSampler;
uniform float utime;


void main()
{
    vec2 sample_pos = vec2(textureCoord.x + sin(textureCoord.y * 5 + utime) * 0.1, textureCoord.y);
    vec3 myTexture =  vec3(texture(textureSampler, sample_pos)).rgb;
    /*  Multiplying by 10 multiplies everything in the screen. SO the black background remains black...
        but the coloured car is tinted with blue
    */
    fragColor = vec4(myTexture.rg, myTexture.b * 10.0, 1.0);
}