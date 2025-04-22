#version 330 core

//  Fragment colors are specified by the fragColor variable
layout (location=0) out vec4 fragColor;

//  The texture's uv coordinates
in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light
{
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;

vec3 getLight(vec3 color)
{
    vec3 Normal = normalize(normal);
    //  Ambient
    vec3 ambient = light.Ia;

    //  Diffuse
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    //  Specular
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    //  The value 32 determines the strength of shining
    float spec =  pow(max(dot(viewDir, reflectDir), 0), 64);
    vec3 specular = spec * light.Is;

    return color * (ambient + diffuse + specular);
}

void main()
{
    //vec3 color = vec3(uv_0, 0.26);
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;
    //  Because textures' colors are already in non-linear space...
    //  the gamma correction is applied twice to the texture colours
    //  so return texture colours to linear space
    color = pow(color, vec3(gamma));
    color = getLight(color);

    //  Apply gamma correction to final colour value
    color = pow(color, 1/vec3(gamma));
    fragColor = vec4(color, 1.0);
}
