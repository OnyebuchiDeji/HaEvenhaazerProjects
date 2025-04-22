#version 330 core

//  The location specifies the number or index of the attributes being passed...
//  Into the shader from the main program
layout (location=0) in vec2 in_texcoord_0;
layout (location=1) in vec3 in_normal;
layout (location=2) in vec3 in_position;

//  Output variable for the rasterized texture coordinates for the fragment shader:
//  Causing fragment shader to have access to the uv coordinates
out vec2 uv_0;
out vec3 normal;
out vec3 fragPos;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

void main()
{
    uv_0 = in_texcoord_0;
    //  Calculate postion of fragment in world space
    fragPos = vec3(m_model * vec4(in_position, 1.0));
    /*
        The inverse and transpose are done for the lighting to be correct even when the model...
        is not uniformly scaled.
    */
    normal = mat3(transpose(inverse(m_model))) * normalize(in_normal);
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}