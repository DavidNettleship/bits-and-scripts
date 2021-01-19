public class Example extends Example2 {

    String name;

    public void sayName(){
        System.out.println("default");
    }

    public String sayName(String name){
        System.out.println(name);
        return name;
    }

    public static void main(String[] args){
        Example e1 = new Example();
        e1.sayExample();
        e1.sayName();
    }

}

public class Example2 {

    public void sayExample(){
        System.out.println("example!");
    }

}