/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Ebenezer Ayo-Meti
 * 
 * Most recent: Wed-21-Feb-2024
 */

import java.io.*;

class Task1
{
    int[] fileIntegersBuffer = null;
    int numberOfIntegersRead = 0;
    private String filePath = "";
    
    public Task1(String filePath)
    {
        fileIntegersBuffer = new int[50];
        this.filePath = filePath;
        this.read_file();
    }
    
    public int[] getIntegerBuffer()
    {
        /*
            This returns the whole buffer, including the zeros that show...
            that those parts have not been given a value
        */
        return fileIntegersBuffer;
    }
    public int[] getBufferData()
    {
        /*
            This only retunrs a buffer that contains the data of the fileIntegerBuffer member
        */
        int[] intBuffer = new int[numberOfIntegersRead];
        System.arraycopy(fileIntegersBuffer, 0, intBuffer, 0, numberOfIntegersRead);
        return intBuffer;
    }
    
    public void printArray()
    {
        String buffer = "";
        for (int i = 0; i< numberOfIntegersRead; i++)
        {
            if (i % 50 == 0 && i != 0)
                buffer += "\n";
            if (i == numberOfIntegersRead - 1)
                buffer +=  Integer.toString(fileIntegersBuffer[i]) + "";
            else
                buffer +=  Integer.toString(fileIntegersBuffer[i]) + " ";
        }
        System.out.println(buffer);
        System.out.println("There are " + numberOfIntegersRead + " integers.");
    }
    
    
    
    private void read_file()
    {
        File fileHandle = new File(this.filePath);
        
        boolean endOfFile = false;
        int lineCount = 0;
        
        if (fileHandle.exists())
        {
            try
            {
                BufferedReader br = new BufferedReader(new FileReader(this.filePath));
                
                while(!endOfFile)
                {
                    ++lineCount;
                    String line = br.readLine();
                    //  If line is not empty
                    if (line == null)
                    {
                        endOfFile = true;
                    }
                    else
                    {
                        //  Strip the line
                        line = line.strip();
                        //  Add the integer to the right index of array
                        appendToArray(Integer.parseInt(line));
                        numberOfIntegersRead += 1;
                    }
                }
                System.out.println("File has been read!");
            }
            catch(IOException excptn)
            {
                System.out.println("An Error! Check it! " + excptn.toString());
            }           
        }
    }
    
    private void appendToArray(int datum)
    {
        if (isFull())
        {
            expand();
        }
        fileIntegersBuffer[numberOfIntegersRead] = datum;
    }
    
    private int arrayCapacity()
    {
        return fileIntegersBuffer.length;
    }
    
    private int arraySize()
    {
        return numberOfIntegersRead + 1;
    }
    
    private boolean isFull()
    {
        return (arraySize() == arrayCapacity());
    }
    
    private void expand()
    {
        int[] newBuffer = new int[fileIntegersBuffer.length * 2];
        
        //  Copy contents of old buffer into new one
        System.arraycopy(fileIntegersBuffer, 0, newBuffer, 0, fileIntegersBuffer.length);
        
        //  Now reassign the fileIntegersBuffer array
        fileIntegersBuffer = newBuffer;
        System.out.println("Successful expansion! Capacity: " + this.arrayCapacity());
    }
}

class Search
{
    static int call_count = 0;
    public static int linearFindMax(int[] data)
    {
        System.out.println("Finding Max Value!");
        int result = data[0];
        
        for (int i = 1; i < data.length; i++)
        {
            if (data[i] > result)
            {
                result = data[i];
            }
        }
        return result;
    }
    
    @SuppressWarnings("empty-statement")
    public static int findTargetVal(int targetVal, int[] data, int stopIndex)
    {
        System.out.println("'Naive' Lineat Search!");
        int i;
        for (i=0; data[i]!=targetVal && i < stopIndex; i++);
        
        if (i==stopIndex)
        {
            return -1;  //  Value not found because it has reached the end
        }
        else
        {
            return i;   //  Index of element found
        }
    }
    
    @SuppressWarnings("empty-statement")
    public static int sentinelFindTargetVal(int targetVal, int[] data, int stopIndex)
    {
        System.out.println("Sentinel Search!");
        int i;
        int stopIndexValStore = data[stopIndex + 1];
        data[stopIndex + 1] = targetVal;    //  The sentinel
        //  The loop stops when the targetVal is hit
        for (i=0; data[i]!=targetVal; i++);
        
        //  If the index is the stop index, the end, then thet target value was not found
        if (i>=stopIndex)
        {
            data[stopIndex + 1] = stopIndexValStore;
            return -1;  //  Value not found because it has reached the end
        }
        else
        {
            data[stopIndex + 1] = stopIndexValStore;
            return i;   //  Index of element found
        }
    }
    
    public static int binary_search(int targetVal, int[] data)
    {
        System.out.println("Normal Binary Search!");
        /*
            This sorting method is ideal for already sorted data...
            such that the data in alphanumeric succession, either ascending or descending.
        */
        int top = data.length-1, bottom = 0, middle;
        
        while (top > bottom)
        {
            middle = (top + bottom) / 2;
            if (data[middle] < targetVal)
                bottom = middle + 1;
            else
                top = middle;
        }
        
        if (top == -1)
            return -2;
        if (data[top] == targetVal)
            return top; //  Index of value returned
        else
            return -1;  //  Value was never found
    }
    
    public static int binary_search_iterative(int targetVal, int[] data, int bottom, int top)
    {
        call_count += 1;
        if (call_count == 1)
            System.out.println("Iterative Binary Search!");
        int middle; middle = (bottom + top) / 2;
        
        if (bottom > top) return -1;    //  targetValue not found
        else if (targetVal == data[middle]) return middle;
        
        //  If the target value is too big to be at the left or bottom side of the sorted array
        else if (targetVal > data[middle])
            //  search through right of middle only
            return binary_search_iterative(targetVal, data, middle + 1, top);
        //  If the target value is too small for the upper side of array
        else
            return binary_search_iterative(targetVal, data, bottom, middle-1);
            
    }
}


class Sorter
{
    public static int[] bubble_sort(int[] data)
    {
        System.out.println("Bubble Sort!");
        for (int top=data.length-1; top > 0; top--)
        {
            for (int i=0; i<top; i++)
            {
                if (data[i] > data[i+1])
                {
                    int temp = data[i];
                    data[i] = data[i+1];
                    data[i+1] = temp;
                }
            }
        }
        return data;
    }
    
}

class QuickSorter
{
    private final int[] m_data;
    
    public QuickSorter(int[] data)
    {
        m_data = data;
    }
    
    public int[] get_array()
    {
//        quick_sort(0, m_data.length - 1);
        return m_data;
    }
    
    public int[] get_sorted_array()
    {
        System.out.println("'Quick Sort!'");
        quick_sort(0, m_data.length - 1);
        return m_data;
    }
    
    private int quick_sort_partition( int left, int right)
    {
        /*
            This is to sort the array and to set the pivot value in the array.
            The pivot value is a value that has been positioned in the array with all the...
            values to its left in the array smaller than it and those in its right larger than it.
            Though it partially sorts the values, not all the values to the left or the right are rightly sorted...
            This is why this method is called recursively by the quicksSort method, after the first partition value is gotten...
            so that the left and right sides to the partition value can be sorted with the same process.
        */
        while (true)
        {
            //  Star
            while (left < right && m_data[left] < m_data[right]) right--;
            if (left < right)
            {
                int temp = m_data[right];
                m_data[right] = m_data[left];
                m_data[left] = temp;
                left++;
            }
            else
                return left;
            while (left < right && m_data[left] < m_data[right]) left++;
            if (left < right)
            {
                int temp = m_data[left];
                m_data[left] = m_data[right];
                m_data[right] = temp;
                right--;
            }
            else
                return right;
        }
    }
    
    
    private void quick_sort(int left, int right)
    {
        if (left >= right) return;
        
        int pivotIndex = quick_sort_partition(left, right);
        
        quick_sort(left, pivotIndex - 1);
        quick_sort(pivotIndex + 1, right);
    }
}


public class Searching_Sorting_DejiWk11
{
    public static void main(String[] args)
    {
        task3B();
    }
    
    public static void task1()
    {
        Task1 t1 = new Task1("src/284652.txt");
        t1.printArray();
    }
    
    public static void task2()
    {
        System.out.println("\n");
        
        Task1 t1 = new Task1("src/284652.txt");
        t1.printArray();
//        System.out.println("\n");
        
        int[] intBuffer = t1.getIntegerBuffer();
        
        //  Naive linear search
        
        //  Find max value in parsed integer buffer
        int maxVal = Search.linearFindMax(intBuffer);
        System.out.println("Maimum value in integer buffer: " + maxVal);
        
        //  Naive search for a target value
        int targetValIndex = Search.findTargetVal(153, intBuffer, intBuffer.length-1);
        if (targetValIndex != -1)
        {
            System.out.println("Target value is indeed in buffer at index " + targetValIndex);
        }
        else
        {
            System.out.println("Doesn't exist!");
        }
        
        //  Senitinel search for target value
        //  Reason for doing -2 from the stop index is because of how sentinel search works....
        //  It makes use of the last space/index in the buffer. It will be better to implement...
        //  this in the function itself though. But I leave it as it is.

        int valInd = Search.sentinelFindTargetVal(158, intBuffer, intBuffer.length-2);
        if (valInd != -1)
        {
            System.out.println("The Item is in the array at index " + valInd);
        }
        else
        {
            System.out.println("The Item is not in the array!");        
        }
    }
    
    public static void task3A()
    {
        System.out.println("\n");
        
        Task1 t1 = new Task1("src/284652.txt");
        System.out.println("Original array: ");
        t1.printArray();
        //  Not the difference when sorted between getting the integer buffer...
        int[] intBuffer = t1.getIntegerBuffer();
        //  and getting the buffer with the data
        int[] bufferData = t1.getBufferData();
        
        int[] sortedBuffer = Sorter.bubble_sort(intBuffer);
        int[] sortedBuffer2 = Sorter.bubble_sort(bufferData);
        System.out.println("Bubble sorted array: " + array_as_string(sortedBuffer));
        System.out.println("Bubble sorted array: " + array_as_string(sortedBuffer2));
        
        QuickSorter qsort = new QuickSorter(intBuffer);
        QuickSorter qsort2 = new QuickSorter(bufferData);
        System.out.println("Quick sorted array: " + array_as_string(qsort.get_sorted_array()));
        System.out.println("Quick sorted array: " + array_as_string(qsort2.get_sorted_array()));
        
    }
    
    public static void task3B()
    {
        ///________BINARY SORT_______///
        System.out.println("\n");  
        Task1 t1 = new Task1("src/284652.txt");
        
        int[] bufferData = t1.getBufferData();
        
        int[] sortedBuffer1 = Sorter.bubble_sort(bufferData);
        
        QuickSorter qsort = new QuickSorter(bufferData);
        int[] sortedBuffer2 = qsort.get_sorted_array();
        
        //  Binary Search Normal
        int valIndex1 = Search.binary_search(38, sortedBuffer1);
        if (valIndex1 != -1)
        {
            System.out.println("The Item is in the array at index at index " + valIndex1);
        }
        else
        {
            System.out.println("The Item is not in the array!");        
        }
        
        //  Binary Search Iterative
        int valIndex2 = Search.binary_search_iterative(178, sortedBuffer2, 0, sortedBuffer2.length - 1);
        if (valIndex2 != -1)
        {
            System.out.println("The Item is in the array at index " + valIndex2);
        }
        else
        {
            System.out.println("The Item is not in the array!");        
        }
    }
        
    public static String array_as_string(int[] arr)
    {
        String array = "";
        for (int i=0; i < arr.length ; i++)
        {
            if (i != arr.length - 1)
                array += Integer.toString(arr[i]) + ", ";
            else
                array += Integer.toString(arr[i]);
        }
        
        return array;
    }
    
    public static void search_tests()
    {
        int[] arr = {0, 1, 2, 3, 4, 5, 8, 9, 72, 18, 100};
        System.out.println(Search.linearFindMax(arr));
        
        int valIndex = Search.findTargetVal(13, arr, arr.length-1);
        if (valIndex != -1)
        {
            System.out.println("The Item is in the array: " + arr[valIndex]);        
        }
        else
        {
            System.out.println("The Item is not in the array!");        
        }
        
        int valInd = Search.sentinelFindTargetVal(8, arr, arr.length-2);
        if (valInd != -1)
        {
            System.out.println("The Item is in the array: " + arr[valInd]);        
        }
        else
        {
            System.out.println("The Item is not in the array!");        
        }
     
    }
    
    public static void sort_tests()
    {
        int[] arr = {9, 10, 78, 54, 34, 100, 91, 39, 10};
        System.out.println("The sorted array: " + array_as_string(Sorter.bubble_sort(arr)));
        
        int[] arr2 = {9, 10, 78, 54, 34, 100, 91, 39, 10};
        
        QuickSorter qsort = new QuickSorter(arr2);
        String aS = array_as_string(qsort.get_array());
        System.out.println("Converted this array: " + aS + "...");
        String sortedArrayAsString = array_as_string(qsort.get_sorted_array());
        System.out.println("Into this the sorted form of the array, quicksorted: " + sortedArrayAsString);
    }
    
}
