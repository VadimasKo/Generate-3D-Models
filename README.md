# Generate 3D models using python
In this repository I post python code which generates 3D models in ".off"format.
## How does .off format work?
  .off file structure is very simple:
  * First line (optional): the letters OFF to mark the file type.
  * Second line: the number of vertices, number of faces, and number of edges, in order
    *  (the latter can be ignored by writing 0 instead).
  * List of vertices: X, Y and Z coordinates.
  * List of faces: number of vertices, followed by the indexes of the composing vertices, in order (indexed from zero).
    * Optionally, the RGB values for the face color can follow the elements of the faces.
  
  Cube example:
    ![cubeOFF](https://user-images.githubusercontent.com/54241089/117651984-488a4300-b19b-11eb-9d0f-c873150abf7c.png)
    ![cube3D](https://user-images.githubusercontent.com/54241089/117651973-4627e900-b19b-11eb-95ee-3712f6e1c834.png)

