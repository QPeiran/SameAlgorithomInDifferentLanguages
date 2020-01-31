using System;

namespace MyApplication
{
  class AnotherProgram
  {
	protected internal void MyMethod2()
    {
      Console.WriteLine("Here's another execution! HaHa  \n ");
    }  
  }  
	
  class Program
  {
    static void MyMethod()
    {
      Console.WriteLine("I just got executed!");
    }

    static void Main(string[] args)
    {
      MyMethod();
	  AnotherProgram methoding = new AnotherProgram();
	  Point Point1 = new Point(1,4);
	  int Sum = Point.Add(Point1);
	  //Console.WriteLine(Point1.x);
	  Console.WriteLine("Adding two points will be: {0} \n",Sum);
	  Person P1 = new Person();
	  P1.nameSetting("s1");
	  string pName = P1.nameGetting();
	  Console.WriteLine("Student Name is : {0}\n", pName);	
	  P1.MyMethod2();
    }
  }
	public class Point
	{
		private int X, Y;
		public Point(int x, int y) 
		{
			X = x;
			this.Y = y; // it's ok to with "this"
		}
		public static int Add(Point point){
			return (point.X + point.Y);
		}
		public static int showID(Person P) 
		{
			return P.ID;
		}
	}  
	public class Person
	{
		/*public string FirstName
		{
			get => firstName;
			set => firstName = (!string.IsNullOrWhiteSpace(value)) ? value : throw new ArgumentException("First name must not be blank");
		}*/
		public int ID = 100;
		private string _firstName = "Default!";
		public void nameSetting (string Name)
		{
			if (string.IsNullOrEmpty(Name)) {throw new ArgumentException("the name is empty!");}
			this._firstName = Name;
		}
		public string nameGetting()
		{
			return _firstName;
		}
		public void MyMethod2()
    	{
      		Console.WriteLine("Here's another execution! HaHa  \n " + Point.showID(this));
    	} 
	}
//	public class 3DPoint: Point
//	{
		
//	}
}
