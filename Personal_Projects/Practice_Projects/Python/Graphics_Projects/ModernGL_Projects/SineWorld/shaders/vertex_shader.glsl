#version 330 core

//  Vertices are sent to rasterization process
layout(location = 0) in vec2 in_position;


void main()
{
    //  Rasterization process breaks the plane into fragments
    gl_Position = vec4(in_position, 0.0, 1.0);
}