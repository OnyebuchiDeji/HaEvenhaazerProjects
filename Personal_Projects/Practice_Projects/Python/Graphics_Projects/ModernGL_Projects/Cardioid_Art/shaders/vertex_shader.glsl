#version 430    //  GLSL language version used

in vec3 in_position;        //  screen plane vertex coordinates (transferred from vertex buffer)

void main()
{
    gl_Position = vec4(in_position, 1);
}