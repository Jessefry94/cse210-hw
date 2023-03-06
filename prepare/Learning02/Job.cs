using System;

public class Job
{
    public string _company;
    public string _jobTitle;
    public int _startYear;
    public int _endYear;

    public void Display()
    {
        Console.WriteLine($" I worked for {_company} as a {_jobTitle} from {_startYear}-{_endYear}");
    }
}