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
	  Point3D P2 = new Point3D(5,7,11);  
	  Console.WriteLine("Adding three points will be: {0} \n", Point3D.Add(P2));
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
	public class Point3D : Point
	{
		public int x,y,z;
		public Point3D(int A, int B, int C) : 
			base(A, B) 
		{
			this.x = A;
			this.y = B;
			this.z = C;
		}
		public static int Add(Point3D P){ //overridding
			return (P.x + P.y + P.z);
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
}
