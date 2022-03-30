/*Extra Credit Event 3/15/21*/

class Student {
     /* fields */
     private String name;
     private String artist;
     private double time; 
     private int year;
     
     /* constructor */
    public music(String name, String artist, double time, int year) {
         this.name = name;
         this.artist = artist;
         this.time = time; 
         this.year = year; 
      }	 	 

     /* accessors */
     public String getName() { return this.name; }
     public String getArtist() { return this.artist; }
     public double getTime() { return this.time; }
     public int getYear() { return this.year; }

 }
class main {
  public static void main(String[] args) {
    system.out.println("Hello world")
music song1 = new music("godsplan","Drake", 1.19.2018);
music song2 = new music("sickmode","Travis Scott", 8.3.2018);
System.out.println(song1.getYear());
System.out.println(song2.getYear());
 
    }     