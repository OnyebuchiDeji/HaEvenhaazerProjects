import glm
import pygame as pg

FOV = 100
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.07
class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        #   View matrix
        ##  Used to control where the camera looks from
        self.m_view = self.get_view_matrix()
        ##  Used to add effects of depth and perspective
        #   Projection Matrix
        self.m_proj = self.get_projection_matrix()

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        ##  To update view matrix after moving
        self.m_view = self.get_view_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        ##  Limiting pitch movement to prevent unnatural movements up and down
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        ##  Because the forward vectir is responsible for camera's orientation...
        ##  using geometry where the forward vector is like the resultant vector, and z and x are the right and up...
        ##  and one where forward is the resultant but now, y and x or z are the others
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self):
        ##  glm.lookAt(eye, center, up) -> glm.mat4
        ##  eye - camera position
        ##  center - position of where camera is looking atexit
        ##  Normalized up vector, how the camera is oriented
        #
        ##return glm.lookAt(self.position, glm.vec3(0), self.up)
        #   The above was changed after camera controls were added because pf the fact that the camera was always looking...
        #   at the model's centre, its movement was being affected because its orientation was...
        #   fixed to the camera's centre
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)