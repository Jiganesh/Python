import java.util.Scanner;

public class OOPsProblem13{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        PrimeManagement[] pm = new PrimeManagement[4];
        for (int i =0 ; i<4 ;i++){
            int primeId = sc.nextInt();
            sc.nextLine();
            String userProfileName = sc.nextLine();
            String subscriptionType = sc.nextLine();
            double subscriptionPrice = sc.nextDouble();
            int noOfProfile = sc.nextInt();
            pm[i] = new PrimeManagement(primeId,userProfileName,subscriptionType,subscriptionPrice,noOfProfile);
        }
        sc.nextLine();
        String typeProvided = sc.next();

        int price = (int)findAvgPriceByType(pm, typeProvided);

        if (price <=0) System.out.println("There are no such prime Management");
        else System.out.println(price);
        sc.close();
        
    }

    public static double findAvgPriceByType(PrimeManagement[] primeManagement, String type){
        double avgPrice = 0;
        int count = 0;
        for(int i = 0; i < primeManagement.length; i++){
            if(primeManagement[i].getSubscriptionType().equals(type) && primeManagement[i].getNoOfProfiles()> 3){
                avgPrice += primeManagement[i].getSubscriptionPrice();
                count++;
            }
        }
        return avgPrice/count;
    }
}

class PrimeManagement{
    private int primeId;
    private String userProfileName;
    private String subscriptionType;
    private double subscriptionPrice;
    private int noOfProfiles;

    public PrimeManagement(int primeId, String userProfileName, String subscriptionType, double subscriptionPrice, int noOfProfiles) {
        this.primeId = primeId;
        this.userProfileName = userProfileName;
        this.subscriptionType = subscriptionType;
        this.subscriptionPrice = subscriptionPrice;
        this.noOfProfiles = noOfProfiles;
    }

    //getter and setter methods
    public int getPrimeId() {
        return this.primeId;
    }

    public void setPrimeId(int primeId) {
        this.primeId = primeId;
    }

    public String getUserProfileName() {
        return this.userProfileName;
    }

    public void setUserProfileName(String userProfileName) {
        this.userProfileName = userProfileName;
    }

    public String getSubscriptionType() {
        return this.subscriptionType;
    }

    public void setSubscriptionType(String subscriptionType) {
        this.subscriptionType = subscriptionType;
    }

    public double getSubscriptionPrice() {
        return this.subscriptionPrice;
    }

    public void setSubscriptionPrice(double subscriptionPrice) {
        this.subscriptionPrice = subscriptionPrice;
    }

    public int getNoOfProfiles() {
        return this.noOfProfiles;
    }

    public void setNoOfProfiles(int noOfProfiles) {
        this.noOfProfiles = noOfProfiles;
    }


}

/*
TestCase1:

1005
Mani
monthly
100
4
1001
Sathish
monthly
300
2
1007
John
yearly
500
5
1003
Joe
monthly
400
5
monthly

*/