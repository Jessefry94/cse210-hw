using System;
public class Fraction
// Creating the class function to create objects that represent functions.
{
    // creating a private integer for top and bottom that can't be accessed 
    // outside of the class
    private int _top;
    private int _bottom;

    public Fraction()
    {
        // This is a contructor that is initializing a new instance with a default value for top
        // and bottom numbers
        _top = 1;
        _bottom = 1;
    }

    public Fraction(int top)
    {
        // This is a contructor that is initializing a new instance with a specified value for top
        // and a default value for bottom numbers
        _top = top;
        _bottom = 1;
    }

    public Fraction(int top, int bottom)
    {
        // This is a contructor that is initializing a new instance with a 
        // specified value for top and bottom numbers.
        _top = top;
        _bottom = bottom;
    }

    // This is a method of the Fraction class which we have been told to call GetFractionString 
    // that returns a string of the fraction in the format "top/bottom" so it will look something like 1/1

    public string GetFractionString()
    // We want to return the formatted string by enclosing the expression.
    {
        return $"{_top}/{_bottom}";
    }


    // Double is being used to get the decimal value.
    public double GetDecimalValue()
    {
        return (double)_top / _bottom;
    }
}
