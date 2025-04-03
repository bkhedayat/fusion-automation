import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        sketchLines = sketch.sketchCurves.sketchLines

        # Draw multiple rectangles in a grid pattern
        spacing = 10  # distance between rectangles
        num_rows = 3
        num_cols = 3
        width = 5
        height = 5
        triangle_base = 4
        triangle_height = 4
        triangle_offset = 2.5  # space between rectangle and triangle

        for row in range(num_rows):
            for col in range(num_cols):
                x = col * spacing
                y = row * spacing
                point1 = adsk.core.Point3D.create(x, y, 0)
                point2 = adsk.core.Point3D.create(x + width, y + height, 0)
                sketchLines.addTwoPointRectangle(point1, point2)

        # Add this below or alongside your rectangle loop
        radius = 2.5  # Radius of the circle

        for row in range(num_rows):
            for col in range(num_cols):
                x = col * spacing + radius
                y = row * spacing + radius
                center = adsk.core.Point3D.create(x, y, 0)
                sketch.sketchCurves.sketchCircles.addByCenterRadius(center, radius)
        
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * spacing
                y = row * spacing
                base_center_x = x + width + triangle_offset
                base_center_y = y + height / 2
                p1 = adsk.core.Point3D.create(base_center_x - triangle_base / 2, base_center_y - triangle_height / 2, 0)
                p2 = adsk.core.Point3D.create(base_center_x + triangle_base / 2, base_center_y - triangle_height / 2, 0)
                p3 = adsk.core.Point3D.create(base_center_x, base_center_y + triangle_height / 2, 0)

                # Draw triangle
                sketchLines.addByTwoPoints(p1, p2)
                sketchLines.addByTwoPoints(p2, p3)
                sketchLines.addByTwoPoints(p3, p1)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
