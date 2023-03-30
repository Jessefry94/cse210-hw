using System;
using System.Collections.Generic;

namespace Shapes
{
    class Program
    {
        static void Main(string[] args)
        {
            var shapes = new List<Shape>();
            shapes.Add(new Square("red", 5));
            shapes.Add(new Rectangle("blue", 2, 4));
            shapes.Add(new Circle("green", 3));

            foreach (var shape in shapes)
            {
                Console.WriteLine($"Color: {shape.GetColor()}, Area: {shape.GetArea()}");
            }
        }
    }
}
// This is how the teacher did theirs
//  List<Shape> shapes = new List<Shape>();

//         Square s1 = new Square("Red", 3);
//         shapes.Add(s1);

//         Rectangle s2 = new Rectangle("Blue", 4, 5);
//         shapes.Add(s2);

//         Circle s3 = new Circle("Green", 6);
//         shapes.Add(s3);

//         foreach (Shape s in shapes)
//         {
//             // Notice that all shapes have a GetColor method from the base class
//             string color = s.GetColor();

//             // Notice that all shapes have a GetArea method, but the behavior is
//             // different for each type of shape
//             double area = s.GetArea();

//             Console.WriteLine($"The {color} shape has an area of {area}.");