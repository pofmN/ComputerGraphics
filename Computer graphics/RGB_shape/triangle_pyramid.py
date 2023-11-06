import glfw
from OpenGL.GL import *

def main():
    # Initialize GLFW
    if not glfw.init():
        print("Failed to initialize GLFW")
        return -1

    # Create a window
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "3D Pyramid", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfw.terminate()
        return -1

    # Set the current context to the created window
    glfw.make_context_current(window)

    # Vertex positions for the pyramid
    vertices = [
        # Front face
        0.0, 1.0, 0.0,  # top vertex
        -1.0, -1.0, 1.0,  # bottom left vertex
        1.0, -1.0, 1.0,  # bottom right vertex

        # Right face
        0.0, 1.0, 0.0,  # top vertex
        1.0, -1.0, 1.0,  # bottom left vertex
        1.0, -1.0, -1.0,  # bottom right vertex

        # Back face
        0.0, 1.0, 0.0,  # top vertex
        1.0, -1.0, -1.0,  # bottom left vertex
        -1.0, -1.0, -1.0,  # bottom right vertex

        # Left face
        0.0, 1.0, 0.0,  # top vertex
        -1.0, -1.0, -1.0,  # bottom left vertex
        -1.0, -1.0, 1.0  # bottom right vertex
    ]

    vertices = GLfloat * len(vertices)(*vertices)

    # Create a Vertex Buffer Object (VBO) and bind to it
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    # Copy vertex data to the VBO
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, vertices, GL_STATIC_DRAW)

    # Create a Vertex Array Object (VAO) and bind to it
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # Specify the layout of the vertex data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
    glEnableVertexAttribArray(0)

    # Vertex Shader
    vertexShaderSource = """
    #version 330 core
    layout (location = 0) in vec3 aPos;
    void main()
    {
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
    }
    """

    # Create a Vertex Shader Object and compile it
    vertexShader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertexShader, vertexShaderSource)
    glCompileShader(vertexShader)

    # Check for vertex shader compile errors
    success = glGetShaderiv(vertexShader, GL_COMPILE_STATUS)
    if not success:
        infoLog = glGetShaderInfoLog(vertexShader)
        print("Vertex shader compilation failed:", infoLog)
        glfw.terminate()
        return -1

    # Fragment Shader
    fragmentShaderSource = """
    #version 330 core
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
    }
    """

    # Create a Fragment Shader Object and compile it
    fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragmentShader, fragmentShaderSource)
    glCompileShader(fragmentShader)

    # Check for fragment shader compile errors
    success = glGetShaderiv(fragmentShader, GL_COMPILE_STATUS)
    if not success:
        infoLog = glGetShaderInfoLog(fragmentShader)
        print("Fragment shader compilation failed:", infoLog)
        glfw.terminate()
        return -1

    # Shader Program
    shaderProgram = glCreateProgram()
    glAttachShader(shaderProgram, vertexShader)
    glAttachShader(shaderProgram, fragmentShader)
    glLinkProgram(shaderProgram)

    # Check for shader program linking errors
    success = glGetProgramiv(shaderProgram, GL_LINK_STATUS)
    if not success:
        infoLog = glGetProgramInfoLog(shaderProgram)
        print("Shader program linking failed:", infoLog)
        glfw.terminate()
        return -1

    # Delete shader objects since they are no longer needed
    glDeleteShader(vertexShader)
    glDeleteShader(fragmentShader)

    # Main Loop
    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Use shader program
        glUseProgram(shaderProgram)

        # Draw pyramid
        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, 12)

        # Swap buffers
        glfw.swap_buffers(window)

        # Poll events
        glfw.poll_events()

    # Clean up resources
    glDeleteVertexArrays(1, vao)
    glDeleteBuffers(1, vbo)
    glDeleteProgram(shaderProgram)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
