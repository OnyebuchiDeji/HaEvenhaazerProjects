#version 330 core

//  Vertices are sent to rasterization process
layout (location= 0) in vec2 vertexPosition;
layout (location=1) in vec2 texturePosition;


out vec2 textureCoords;

void main()
{
    //  Rasterization process breaks the plane into fragments
    textureCoords = texturePosition;
    gl_Position = vec4(vertexPosition, 0.0, 1.0);
}