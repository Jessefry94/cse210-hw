public class Assignment
{
    private string _studentName;
    private string _topic;

    public Assignment(string studentName, string topic)
    {
        _studentName = studentName;
        _topic = topic;
    }

    public string GetSummary()
    {
        return $"Student: {_studentName} - Topic: {_topic}";
    }

    protected string GetStudentName()
    {
        return _studentName;
    }
}
