
vec3 getMaterial(vec3 p, float id, vec3 normal)
{
    vec3 m;
    switch(int(id)){
        case 1:
            m = vec3(0.9, 0.0, 0.0); break;
        case 2:
            m = vec3(0.2 + 0.4 * mod(floor(p.x) + floor(p.z), 2.0)); break;
        case 3:
            m = vec3(0.7, 0.8, 0.9); break;
        case 4:
            vec2 i = step(fract(0.5 * p.xz), vec2(1.0 / 10.0));
            m = ((1.0 - i.x) * (1.0 - i.y)) * vec3(0.37, 0.12, 0.0); break;
        //  Cube
        case 5:
        //  Need to perform the same transformations on the texture
        //  and because of rotation, the normals should also be rotated.
            translateCube(p);
            rotateCube(p);
            rotateCube(normal);
            m = triPlanar(u_texture1, p * cubeScale, normal); break;
        default:
            m = vec3(0.4); break;
    }
    return m;
}