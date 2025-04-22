
package webserver;

/**
 *  Started: Tues-04-March-2025
 *  Finished: Tues-04-March-2025
 * 
 *  Finally, consider these Lambda operations:
 *  
 *  https://stackoverflow.com/questions/13604703/how-do-i-define-a-method-which-takes-a-lambda-as-a-parameter-in-java-8
 *  https://stackoverflow.com/questions/877096/how-can-i-pass-a-parameter-to-a-java-thread
 * 
 * 
 */
import java.io.*;
import java.net.*;
import java.util.*;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.time.*;
import java.time.format.DateTimeFormatter;
import static webserver.ContentHeaderType.IMGPNG;
//import Concurrency.RunnableIntergace;
//import java.text.SimpleDateFormat;

public class WebServer {

    final static String CRLF = "\r\n";
    final static int Port = 9095;

    private static void test1_ImageRead() throws Exception
    {
        //  Test
        File file = new File("src/webserver/image.gif");
        FileInputStream fis = new FileInputStream(file);       
        BufferedImage img = ImageIO.read(fis);
        System.out.println(img.getWidth());
        System.out.println(img.getHeight());
        System.out.println(file.length());
        System.out.println(file.lastModified());
        String info = "Length: %s, Last Modified: %s";
        String dateAsString = new Date(file.lastModified()).toString();
        String[] tkns = dateAsString.split(" ");
        dateAsString = "%s, %s %s %s %s";
        dateAsString = String.format(dateAsString, tkns[0], tkns[2], tkns[1], tkns[3], tkns[4]);
        info = String.format(info, file.length(), dateAsString);
        System.out.println("Image Info:\n" + info);
    }
    
    private static void test2_datetime()
    {
        LocalDateTime dtObj = LocalDateTime.now();
        String currentDate = dtObj.toString();
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("E, dd MMM yyyy HH:mm:ss");
        currentDate = dtObj.format(formatter) + " GMT\r\n";
        System.out.println("Current Date: " + currentDate);
    }
    
    private static void test3_readFile() throws Exception
    {
        File file = new File("src/webserver/Test1.html");
        byte[] buffer = new byte[4096];
        int bytes = 0;
        int bytesRead = 0;

        FileInputStream fis = new FileInputStream(file);
        StringBuilder sb = new StringBuilder("New Byte[] {");
//        // Copy requested file into the socket's output stream.
        while ((bytesRead = fis.read(buffer)) != -1)
        {
            if (bytesRead != -1){
                bytes += bytesRead;
            }
        }
        System.out.println("Length: " + bytes);
        for (int i=0; i<bytes;i++){
            sb.append(buffer[i]);
        }
        sb.append("}");
        System.out.println(sb.toString());
        
        BufferedReader br = new BufferedReader(new FileReader(file));
        StringBuilder sb2 = new StringBuilder();
        String line = "";
        
        while ((line = br.readLine()) != null){
            sb2.append(line);
            sb2.append(System.lineSeparator());
        }
        String fileString = sb2.toString();
        System.out.println(fileString);
        br.close();
        
    }
    public static void main(String argv[]) throws Exception
    {
//        test1_ImageRead();
//        test2_datetime();
//        test3_readFile();
        
        
        //int port = (new Integer(argv[0])).intValue();
//        int port = 9095;
        
        // Establish the listen socket.
        
        //TODO - Task1: Create a TCP server socket using the port above using the serverSocket variable
        ServerSocket serverSocket = new ServerSocket(Port);
        System.out.println("Server is running at port " + Port + " and is waiting for client connection.");
        
        // Process HTTP service requests in an infinite loop.
        while (true) {
            // Listen for a TCP connection request.
            Socket connection = serverSocket.accept();

            // Construct an object to process the HTTP request message.
            WebServer webServer = new WebServer();
            
            //  Not concurrent
//            webServer.processRequestNonAsynchronous(connection);
            //  Concurrent
            webServer.processRequestAsynchronous(connection);
        }
    }

    private String getFileName(BufferedReader br) throws IOException {
        String fileName=null;
        String line=br.readLine();
        //TODO - Task2: Please implement this method to extract the filename from HTTP headers;
        fileName = line.split(" ")[1].replace("/", "");
        return fileName;
    }

    private DataOutputStream os;

    private void processRequestNonAsynchronous(Socket socket)
    {
        try{
            processClientRequest(socket);
        }
        catch (Exception e){
            System.out.println(e.toString());
        }
        
    }
    
    private void processRequestAsynchronous(Socket socket) throws Exception
    {
        try{
            Thread t = new Thread(()->processRequestNonAsynchronous(socket));
            t.start();
            System.out.println("Client Request Processed on Thread: " + t.getName());
        }
        catch(Exception e){
            System.out.println(e.toString());
        }
        
    }    
    private void processClientRequest(Socket socket) throws Exception {
        os = new DataOutputStream(socket.getOutputStream());
        BufferedReader br = receive(socket);
        
        try {
            String fileName=getFileName(br);
            if (fileName==null)
            {
                return;
            }
                
            File file = new File("src/webserver/" + fileName);
            System.out.println("File Requested: "+ fileName);
            
            //  Determine file type
            ContentHeaderType fileType = ContentHeaderType.HTMLTEXT;
            String[] fileNameTokens = fileName.split("[,\\.\\s]");
//            System.out.println("Token1: " + fileNameTokens[0]);
//            System.out.println("Token2: " + fileNameTokens[1]);
            switch(fileNameTokens[1])
            {
                case "txt":
                    fileType = ContentHeaderType.PLAINTEXT;
                    break;
                case "png":
                    fileType = ContentHeaderType.IMGPNG;
                    break;
                case "jpg":
                    fileType = ContentHeaderType.IMGJPEG;
                    break;
                case "jpeg":
                    fileType = ContentHeaderType.IMGJPEG;
                    break;
                case "gif":
                    fileType = ContentHeaderType.IMGGIF;
                    break;
                case "json":
                    fileType = ContentHeaderType.APPJSON;
                    break;
            }
            
            HttpUtilities utl = new HttpUtilities();
            // Construct the response message.

            if (file.exists()) {
                //  This checks if the fileType enum value is less than IMGPNG
                if (fileType.compareTo(ContentHeaderType.IMGPNG) < 0)
                {
                    //TODO - Task3: Construct and send the HTTP header using the "send(String data)" method. The header should include the "request has succeded" status code.
                    //Please refer to the HTTP response format.

                    //  Header message
                    send (utl.ConstructHeaderMessage(file, fileType));
                    send(file);
//                    sendFile(file);
//                    os.flush();
                }
                else{
                    //  Send remaining header message
                    send (utl.ConstructHeaderMessage(file, fileType));
                    sendImage(file);
                }
            } else {
                //TODO - Task5: Construct and send the appropriate HTTP header using the "send(String data)" method. Hint: If the file does not exist then the status code is 404.
                send(utl.GetFileNotFoundHeader());
                send("File Not Found!");
            }
            //TODO - Task6: Extend the application to send PNG files too
            
        } finally {
            os.flush();
            os.close();
            br.close();
            socket.close();
        }
    }


    

    private BufferedReader receive(Socket socket) throws IOException {
        InputStream is = socket.getInputStream();
        // Set up input stream filters.
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        return br;
    }

    private void send(String data) throws IOException {
        os.writeBytes(data);
    }
    
    /**
     *  This reads the files as bytes using a byte stream
     *  and sends each that is read using os.write()
     */
    private void send(File file) throws Exception {
        // Construct a 1K buffer to hold bytes on their way to the socket.
        byte[] buffer = new byte[1024];
        int bytes = 0;

        FileInputStream fis = new FileInputStream(file);
        // Copy requested file into the socket's output stream.
        while ((bytes = fis.read(buffer)) != -1) {
            os.write(buffer, 0, bytes);
        }
        fis.close();
    }
    
    /**
     *  Another method for sending files.
     *  NOte that the strings are sent as bytes.
     *  The byte conversion is done by the `send(String data)`
     *  method, by the os.writeBytes(data);
     */
    private void sendFile(File file) throws Exception
    {
        BufferedReader br = new BufferedReader(new FileReader(file));
        StringBuilder sb = new StringBuilder("");
        String line = "";
        
        while ((line = br.readLine()) != null){
            sb.append(line);
            sb.append(System.lineSeparator());
        }
//        String fileString = sb.toString();
//        System.out.println(fileString);
        send(sb.toString());
        br.close();
    }
        
    
    private void sendImage(File file) throws Exception
    {
        FileInputStream fis = new FileInputStream(file);       
        BufferedInputStream reader = new BufferedInputStream(fis);
        byte[] buffer = new byte[4096];
        int bytesRead;
        while ((bytesRead = reader.read(buffer)) != -1){
            os.write(buffer, 0, bytesRead);
        }
        reader.close();
        fis.close();
        os.flush();
    }
   
}

enum ContentHeaderType{
    HTMLTEXT, PLAINTEXT, IMGPNG, IMGJPEG, IMGGIF, APPJSON
}

class HttpUtilities
{   

    public String GetSuccessHeader()
    {
        return "HTTP/1.1 200 OK\r\n";
    }
    public String GetFileNotFoundHeader()
    {
        return "HTTP/1.1 404 File Not Found\r\n";
    }
    public String GetContentTypeHeader(ContentHeaderType type)
    {
        String base = "Content-Type: %s; charset=ISO-8859-1\r\n\r\n";
        switch (type){
            case HTMLTEXT:
                return String.format(base, "text/html", 1024);
            case PLAINTEXT:
                return String.format(base, "text/plain", 1024);
            case APPJSON:
                return String.format(base, "application/json", 1024);
            case IMGPNG:
                return String.format(base, "image/png", 1024);
            case IMGJPEG:
                return String.format(base, "image/jpeg", 1024);
            case IMGGIF:
                return String.format(base, "image/gif", 1024);
           
        }
        return "";
    }
    
    public String ConstructHeaderMessage(File file, ContentHeaderType fileType) throws Exception
    {
        LocalDateTime dtObj = LocalDateTime.now();
        String currentDate = dtObj.toString();
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("E, dd MMM yyyy HH:mm:ss");
        currentDate = dtObj.format(formatter) + " GMT\r\n";
        
        
        String server = "CustomWebServer/1.0.0 (Windows)\r\n";
        
        String lastModified = new Date(file.lastModified()).toString();
        String[] tkns = lastModified.split(" ");
        lastModified = "%s, %s %s %s %s\r\n";
        lastModified = String.format(lastModified, tkns[0], tkns[2], tkns[1], tkns[3], tkns[4]);
        
        String eTag = "'17dc6-a5c-bf716880'\r\n";
        String acceptRanges = "bytes\r\n";
        String contentLength = file.length() + "\r\n";
        String keepAlive = "timeout=10, max=100\r\n";
        String connection = "Keep-Alive\r\n";
        
        String status = GetSuccessHeader();
        String contentType = GetContentTypeHeader(fileType);
        
        //  read HTML file
//        byte[] buffer = new byte[4096];
//        int bytes = 0;
//        int bytesRead = 0;
//
//        FileInputStream fis = new FileInputStream(file);
//        StringBuilder sb = new StringBuilder("");
//        // Copy requested file into the socket's output stream.
//        while ((bytesRead = fis.read(buffer)) != -1)
//        {
//            if (bytesRead != -1){
//                bytes += bytesRead;
//            }
//        }
//        for (int i=0; i<bytes; i++){
//            sb.append(buffer[i]);
//        }
//        BufferedReader br = new BufferedReader(new FileReader(file));
//        StringBuilder sb = new StringBuilder("");
//        String line = "";
//        
//        while ((line = br.readLine()) != null){
//            sb.append(line);
//            sb.append(System.lineSeparator());
//        }
//        String fileString = sb.toString();
//        System.out.println(fileString);
//        br.close();
    
        String msg = String.format("%s%s%s%s%s%s%s%s%s%s",
                                    status,currentDate,
                                    server, lastModified,
                                    eTag, acceptRanges,
                                    contentLength, keepAlive,
                                    connection, contentType);
//        System.out.println(msg);
        return msg;
    }
}