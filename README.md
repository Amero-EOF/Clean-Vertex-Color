[![](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/114952874177462273)
# Clean Vertex Color (Blender Addon)
Select Vertex Color is an addon for blender that both selects an object by vertex color, and limited dissolves the vertex colors individual for quick triangle reduction.

My intentions were to quickly create an addon for blender that would improve modelling workflow between MagicaVoxel -> Blender -> Roblox.


## Instructions
1. Export model as .ply format from MagicaVoxel.
2. Import model to blender as .ply
3. Select the object in Blender, and go into `Edit` mode.
4. Open the N-Menu on the right side of the viewport by using the `N` hotkey.
5. Select `Clean Vertex Color` from the list. ( Yea, I should definitely rename that ) 
6. After the menu is opened press the `Clean Vertex Color` button to clean the mesh.

<br>

### Notes

<hr>

This addon is valuable because it enables sharp lines for vertex colors, which is not commonly used. 
It's mostly useful when working with voxelated models. The addon maintains distinct color boundaries 
without any gradation, enhancing the visual clarity of voxelated models. In summary, this addon's 
ability to retain sharp lines for vertex colors greatly improves the appearance.

<br>

### Why use vertex color when `Diffuse Maps`/`Color Maps` already exist even on a platform like Roblox?

<hr>

To answer this question, I have to explain the limitations of the Roblox engine. Currently on Roblox
we are limited to use an object called SurfaceAppearance which provides some PBR capabilities, including
Metalness, Roughness, Normal, and Color Maps. These maps are great, but unfortunately we lack the ability
to use some of Robloxes built in materials like Glass, Forcefields, and Neon. It is not well-known that
meshes with vertex coloring have the capability of using built in materials while also including the colors
from the mesh, an example is shown below:

<br>

#### Basic Vertex Coloring
> Here is a helmet I made in MagicaVoxel that uses vertex coloring, and the default Roblox SmoothPlastic material, exported from blender using. <br><br>
> <img width="685" alt="RobloxStudioBeta_2AQss5oLQ6" src="https://github.com/Amero-EOF/Select-Vertex-Color/assets/60054103/523de928-149b-4f10-bc8f-8b71627714b7">

<br>

#### Vertex Coloring W/ Neon
> Once again the Helmet with Robloxes built in Neon material. <br><br>
> <img width="730" alt="RobloxStudioBeta_3QgbUpzuvH" src="https://github.com/Amero-EOF/Select-Vertex-Color/assets/60054103/d66739e1-4693-43a7-8427-310bbaf2c6fc">

<br>

#### SurfaceAppearance/TextureID

> Now here is an example using a SurfaceAppearance, the results of using the TextureID property of the mesh are the same. <br><br>
> ![image](https://github.com/Amero-EOF/Select-Vertex-Color/assets/60054103/ec1af40c-bb42-4685-91c6-753963243a67)
