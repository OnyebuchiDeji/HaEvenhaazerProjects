import moderngl_window as mglw


class App(mglw.WindowConfig):
    #   This resolution is best because it fits my screen and so doesn't cause the fragmentShader coordinates...
    #   to move
    window_size = 960, 540
    resource_dir = 'shaders'

    ##  Calling super() will automatically create these:
    #   self.ctx - OpenGL context
    #   self.wnd -- the window instance
    #   self.timer -- the timer instance

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #create screen alignment quad
        self.quad = mglw.geometry.quad_fs() ## The screen to display

        #   load shader program
        self.prog = self.load_program(vertex_shader='vertex_shader.glsl',
                                        fragment_shader='fragment_shader.glsl')

        self.set_uniform('resolution', self.window_size)    ##  Sending necessary values to shader input

    #   To pass uniform variables to fragment shader
    def set_uniform(self, u_name, u_value):
        try:
            self.prog[u_name] = u_value
        except KeyError:
            print(f'uniform: {u_name} - not used in shader')

    def render(self, time, frame_time):
        self.ctx.clear()    # Clear frame buffer
        self.set_uniform('time', time)
        self.quad.render(self.prog)

if __name__ == '__main__':
    mglw.run_window_config(App)

##  Shaders are programs that take advantage of parallel computing on the GPU.
##  They participate in different stages of the OpenGL Graphics pipeline and are..
##  Written in the glsl language

