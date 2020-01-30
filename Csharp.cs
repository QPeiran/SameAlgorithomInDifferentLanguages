using System;

namespace MyApplication
{
  class AnotherProgram
  {
	protected internal void MyMethod2()
    {
      Console.WriteLine("Here's another execution! HaHa");
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
	  methoding.MyMethod2();
	  Point Point1 = new Point(1,4);
	  int Sum = Point.Add(Point1);
	  //Console.WriteLine(Point1.x);
	  Console.WriteLine(Sum);
    }
  }
	public class Point
	{
		public int x, y;
		public Point(int x, int y) 
		{
			this.x = x;
			this.y = y;
		}
		public static int Add(Point point){
			return (point.x + point.y);
		}
	}  
//	public class 3DPoint: Point
//	{
		
//	}
}
