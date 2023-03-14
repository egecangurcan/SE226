import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

class Main {

    private static Map<String, int[]> districtStatistics = new HashMap<String, int[]>();
    private static int[] totalStatistics = new int[2];

    public static void main(String[] args) {

        List<String> csvFiles = new ArrayList<>();

        File folder = new File("csv");
        File[] files = folder.listFiles();

        // add all CSV files to the list
        for (File file : files) {
            if (file.isFile() && file.getName().endsWith(".csv")) {
                csvFiles.add(file.getPath());
            }
        }

        // create a thread for each file and start processing
        List<Thread> threads = new ArrayList<Thread>();
        for (String file : csvFiles) {
            Thread t = new Thread(new BusStatisticsThread(file));
            t.start();
            threads.add(t);
        }

        // wait for all threads to finish
        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // display the results
        System.out.println("District"+"                Total Passangers"+"        Avg Passangers");

        System.out.println("------------------- "+"     -----------"+"          --------------");
        for (String district : districtStatistics.keySet()) {
            int[] stats = districtStatistics.get(district);
            System.out.println(district + "          " + stats[0] + "              " + stats[1]);
        }
        System.out.println("Total            " + totalStatistics[0] + "             " + totalStatistics[1]);
    }

    public static class BusStatisticsThread implements Runnable {

        private String fileName;
        private String district;
        private int totalPassengers;
        private int numDays;

        public BusStatisticsThread(String fileName) {
            this.fileName = fileName;

            String[] parts = fileName.split("\\\\"); // split using backslash as delimiter
            this.district = fileName;
        }

        @Override
        public void run() {
            try {
                Scanner scanner = new Scanner(new File(fileName));
                int totalPassengers = 0;
                int numDays = 0;
                while (scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    if (!line.startsWith("Date")) {
                        String[] values = line.split(",");
                        totalPassengers += Integer.parseInt(values[3]);
                        numDays++;
                    }
                }
                scanner.close();
                int[] stats = new int[2];
                stats[0] = totalPassengers;
                stats[1] = totalPassengers / numDays;
                synchronized (districtStatistics) {
                    districtStatistics.put(district, stats);
                    // update the total statistics
                    totalStatistics[0] += stats[0];
                    totalStatistics[1] += stats[1];
                }
                // display the results for this district
                System.out.println(district + "\t" + stats[0] + "\t" + stats[1]);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }
    }

}
