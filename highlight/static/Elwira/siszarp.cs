// Elwira Lichocka
using System;

interface InterfaceA
{
    int Counter { get; }
}

interface InterfaceB
{
    int Counter { get; }
}

class ClassA
{
    protected static int counter;

    public ClassA()
    {
        counter++;
    }

    virtual public string GetMyName()
    {
        return "ClassA";
    }
}

class ClassB : ClassA
{
    new protected static int counter;
    protected string text;

    public ClassB()
    {
        counter++;
        text = "";
    }

    protected ClassB(string text)
    {
        counter++;
        this.text = text;
    }

    virtual public Object Create(string text)
    {
        return new ClassB(text);
    }
}

class Test1
{
    public static void PrintCounterA(InterfaceA a)
    {
        System.Console.Out.WriteLine(a.Counter);
    }

    public static void PrintCounterB(InterfaceB b)
    {
        System.Console.Out.WriteLine(b.Counter);
    }

    public static void PrintName(ClassA a)
    {
        System.Console.Out.WriteLine(a.GetMyName());
    }
}

class MyClass : ClassB, InterfaceA, InterfaceB {
 public MyClass(string b) { this.text=b; }
 public MyClass() { this.text=""; }
 
 public override string GetMyName(){
 return base.GetMyName() + "MyClass" + this.text; 
 }
 
 public static void DestroyObject(Object o) { 
 	if(o is ClassB) { ClassA.counter--; }
 	if(o is MyClass) {
 		ClassA.counter--;
 		ClassB.counter--;
 	}
 }
 
 int InterfaceA.Counter { get { return ClassA.counter; } }
 
 int InterfaceB.Counter { get { return ClassB.counter; } }
 
 public void Print(){
 this.GetMyName();
 System.Console.Out.WriteLine("\n");
 }
 
 public void Print(int n){
 	for (int i=0; i < n; i=i+1){
 		this.GetMyName();
 		System.Console.Out.WriteLine("\n");
 	}
 }
 
public static bool op_Equality(MyClass a, MyClass b){
 		return (a.text).Equals(b.text);
	}
 
 public static bool op_Inequality(MyClass a, MyClass b){
 	return (!(a.text).Equals(b.text));
 }
 
 public void PrintCounter(Type type){
 	if(type == typeof(ClassA)) {
 		System.Console.Out.WriteLine(ClassA.counter);
 		System.Console.Out.WriteLine("\n"); }
 	if(type == typeof(ClassB)) {
 		System.Console.Out.WriteLine(ClassB.counter);
 		System.Console.Out.WriteLine("\n"); }
 			else {
 				System.Console.Out.WriteLine("null\n");}
  }
 
 public override Object Create(string text)
    {
        return new MyClass(text);
    }
 }
 

class MyOtherClass : ClassA {
public override string GetMyName(){
return base.GetMyName() + "MyOtherClass";
}
}

class M {
	public static void Main(string[] args)
{
MyClass mc = new MyClass("test");
MyOtherClass moc = new MyOtherClass();
Test1.PrintCounterA(mc);
Test1.PrintCounterB(mc);
ClassA a = new ClassA();
ClassB b = new ClassB();
Test1.PrintCounterA(mc);
Test1.PrintCounterB(mc);
Test1.PrintName(mc);
Test1.PrintName(moc);
MyClass.DestroyObject(mc);
Test1.PrintCounterA(mc);
Test1.PrintCounterB(mc);
MyClass.DestroyObject(moc);
mc.PrintCounter(typeof(ClassA));
mc.PrintCounter(typeof(ClassB));
mc.PrintCounter(typeof(string));
mc.Print(2);
(mc.Create("new MyClass") as MyClass).Print();
System.Console.Out.WriteLine(mc == ((MyClass)mc.Create("test")));
}
}
