#version 430

out vec4 fragColor;

uniform vec2 resolution;
uniform float time;

const float PI = acos(-1.0);

//  A function to rotate a given vector along an angle
vec2 rotate2D(vec2 uv, float a)
{

  float s = sin(a);
  float c = cos(a);

  //  The roatation matrix and multiplying the vector by it.
  //  Allowing the rotation of any 2D vector
  return mat2(c, -s, s, c) * uv;

}

//  Random number generator function that produces a random 2D vector to be added to col variable
vec2 hash12(float t)
{
  float x = fract(sin(t * 3453.329));
  float y = fract(sin((t + x) * 8532.732));

  return (x, y);
}


vec4 colorChangingCardioid(vec2 uv, vec3 col)
{
  //  Cardioid radius
  float r = 0.17;
  
  //  It is this loop that causes the brightness of the colors, the longer the loop...
  //  the greater the color accummulation or sum; thus, the brighter the color
  for (float i=0.0; i < 60.0; i++)
  {

    float a = i / PI;
    float dx = 2 * r * cos(a) - r*cos(2*a);
    float dy = 2 * r * sin(a) - r*sin(2*a);

    col += 0.01 / length(uv - vec2(dx + 0.1, dy));
  }

  /*  Changing colour of shape by multiplying the colour variable by any color needed.
      The function or expression used in col is from y2:
      y1 = sin(x)
      y2 = 0.15*y1 + 0.25 //  Doing this causes smoothe colour change
      In this case, x = vec3(0.2, 0.8, 0.9) * time
  */

  //  The time here controls how fast the colours change. Multiplying by ten makes it go very fast
  col *= sin(vec3(0.2, 0.8, 0.9) * time * PI) * 0.15 + 0.25;

  return vec4(col, 1);  //  The second parameter is the alpha value, so is vec4
}

vec4 movingColorChangingCardioid(vec2 uv, vec3 col)
{

  float r = 0.17;
  
  for (float i=0.0; i < 60.0; i++)
  {
    //  A factor variable that changes values according to a periodic function
    float factor = (sin(time) * 0.5 + 0.5) + 0.3;
    i += factor; // Tie factor to i

    float a = i / 3;
    float dx = 2 * r * cos(a) - r*cos(2*a);
    float dy = 2 * r * sin(a) - r*sin(2*a);

    col += (0.01 * factor) / length(uv - vec2(dx + 0.1, dy));
  }

  //  Changing colour of shape by multiplying the colour variable by any color needed.
  //  Thw functio or expression used in col is from y2:
  //  y1 = sin(x)
  //  y2 = 0.15*y1 + 0.25 //  Doing this causes smoothe colour change
  //  In this case, x = vec3(0.2, 0.8, 0.9) * time
  col *= sin(vec3(0.2, 0.8, 0.9) * time) * 0.15 + 0.25;

  return vec4(col, 1);  //  The second parameter is the alpha value, so is vec4
}

vec4 differentShape(vec2 uv, vec3 col)
{
  float r = 0.17;

  for (float i=0.0; i < 60.0; i++)
  {
    //  A factor variable that changes values according to a periodic function
    float factor = (sin(time) * 0.5 + 0.5) + 0.3;
    i += factor; // Tie factor to i

    float a = i / 3;
    float dx = 2 * r * cos(a) - r*cos(2*a);
    float dy = 2 * r * sin(a)*cos(a) + r*sin(2*a); //  Shape made from changing '-' to '+'

    col += (0.01 * factor) / length(uv - vec2(dx + 0.1, dy));
  }

  //  Changing colour of shape by multiplying the colour variable by any color needed.
  //  Thw functio or expression used in col is from y2:
  //  y1 = sin(x)
  //  y2 = 0.15*y1 + 0.25 //  Doing this causes smoothe colour change
  //  In this case, x = vec3(0.2, 0.8, 0.9) * time
  col *= sin(vec3(0.2, 0.8, 0.9) * time) * 0.15 + 0.25;

  return vec4(col, 1);  //  The second parameter is the alpha value, so is vec4
}

vec4 gitteringCardioid(vec2 uv, vec3 col)  //  Uses hash12() random vec2 generator
{
  float r = 0.17;

  for (float i=0.0; i < 60.0; i++)
  {
    //  A factor variable that changes values according to a periodic function
    float factor = (sin(time) * 0.5 + 0.5) + 0.3;
    i += factor; // Tie factor to i

    float a = i / 3;
    float dx = 2 * r * cos(a) - r*cos(2*a);
    float dy = 2 * r * sin(a) - r*sin(2*a); //  Shape made from changing '-' to '+'

    col += (0.01 * factor) / length(uv - vec2(dx + 0.1, dy) - 0.02 * hash12(i));
  }

  //  Changing colour of shape by multiplying the colour variable by any color needed.
  //  Thw functio or expression used in col is from y2:
  //  y1 = sin(x)
  //  y2 = 0.15*y1 + 0.25 //  Doing this causes smoothe colour change
  //  In this case, x = vec3(0.2, 0.8, 0.9) * time
  col *= sin(vec3(0.2, 0.8, 0.9) * time) * 0.15 + 0.25;

  return vec4(col, 1);  //  The second parameter is the alpha value, so is vec4
}

void main(){

  //  So that the shader's execution does not depend on the intitial resolution...
  //  Here is a uv vector that is normalized by the value of this resolution and the...
  //  coordinate center is at the center of the screen

  vec2 uv = (gl_FragCoord.xy - (0.5 * resolution.xy)) / resolution.y;

  vec3 col = vec3(0.0);   //  Colour black. It is vec3 because of RGB



  //   Calculating and adding the length of the uv vector is added to the resulting colour
  //col += 0.01 / length(uv);
  //col += 0.01 / length(uv - vec2(0.25));

  //  Applying the rotation function to the whole coordinate system:
  //  EG:
  // uv = rotate2D(uv, time);

  //  Moving coordinate system rotation by 90 degrees
  uv = rotate2D(uv, 3.14 / 2.0);


  fragColor =  colorChangingCardioid(uv, col);
}