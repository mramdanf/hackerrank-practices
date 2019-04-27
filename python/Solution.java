abstract class Car {
    protected boolean isSedan;
    protected String seats;
    
    public Car(boolean isSedan, String seats) {
        this.isSedan = isSedan;
        this.seats = seats;
    }
    
    public boolean getIsSedan() {
        return this.isSedan;
    }
    
    public String getSeats() {
        return this.seats;
    }
    
    abstract public String getMileage();
    
    public void printCar(String name) {
        System.out.println( 
          "A " + name + " is " + (this.getIsSedan() ? "" : "not ") 
            + "Sedan, is " + this.getSeats() + "-seater, and has a mileage of around "
            + this.getMileage() + ".");
    }
}

class WagonR extends Car {
	public WagonR() {
		super(false, "4-seaters");
	}

	public String getMileage() {
		return "22 kmpl";
	}
}

class HondaCity extends Car {
	public HondaCity() {
		super(true, "4-seaters");
	}

	public String getMileage() {
		return "18 kmpl";
	}
}

class InnovaCrysta extends Car {
	public InnovaCrysta() {
		super(true, "2-seaters");
	}

	public String getMileage() {
		return "10 kmpl";
	}
}

public class Solution {
    
    public static void main(String[] args) {
        Car wagonR = new WagonR();
        wagonR.printCar("WagonR");
            
        Car hondaCity = new HondaCity();
        hondaCity.printCar("HondaCity");

        Car innovaCrysta = new InnovaCrysta();
        innovaCrysta.printCar("InnovaCrysta");
    }
}