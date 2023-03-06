using System;

class Program
{
    static void Main(string[] args)
    {
        Job job1 = new Job();
        job1._jobTitle = "Software Engineer";
        job1._company = "Nintendo";
        job1._startYear = 2020;
        job1._endYear = 2022;

        Job job2 = new Job();
        job2._jobTitle = "Server";
        job2._company = "Applebees";
        job2._startYear = 2010;
        job2._endYear = 2012;

        // job1.Display();
        // job2.Display();

        Resume myResume = new Resume();
        myResume._name = "Jesse Fry";

        myResume._jobs.Add(job1);
        myResume._jobs.Add(job2);

        myResume.Display();
    }
}