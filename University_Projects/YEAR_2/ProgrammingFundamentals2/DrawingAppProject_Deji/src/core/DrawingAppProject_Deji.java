/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

package core;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;
import java.util.HashMap;


/**
 *
 * @author Ebenezer Ayo-Meti
 */

//class teach
//{
//    static class myClass implements myInterface
//    {
//    //        @Override
//        public void doSth(String aVal)
//        {
//            System.out.println("My String is " + aVal);
//        }
//    }
//    
//    
//    public interface myInterface
//    {
//        void doSth(String aVal);
//    }
//    
//}


public class DrawingAppProject_Deji
{
    public class Window extends JFrame
    {
        public BorderLayout border = new BorderLayout();
        
        public Window(int width, int height)
        {
            super("My Drawing App");
            setPreferredSize(new Dimension(width, height));
            
        }

        
    }
    
    public class MenuWrapper
    {
        private JMenuBar menuBar = new JMenuBar();
        private HashMap<String, JMenu> Menus = new HashMap<>();
        //  The key is the mennu name, and the value is the menu item name
        private HashMap<String, String> MenuItems = new HashMap<>();
        
        public MenuWrapper(){}
        
        public void add_to_menuBar(String menuName)
        {
            this.menuBar.add(Menus.get(menuName));
        }
        
        public void make_menu(String menuName, JMenu menuObject)
        {
            this.Menus.put(menuName, menuObject);
        }
        
        public void add_menu_item(String menuName, String itemName, JMenuItem menuItem)
        {
            this.Menus.get(menuName).add(menuItem);
            this.MenuItems.put(menuName, itemName);
        }
        
        
        
        
    }
    
    public class MenuManager
    {
        private JMenuBar menuBar = new JMenuBar();
        private HashMap<String, JMenu> Menus = new HashMap<>();
        //  The key is the mennu name, and the value is the menu item name
        private HashMap<String, String> MenuItems = new HashMap<>();
        
        public MenuManager(){}
        
        public JMenuBar access_menuBar()
        {
            return this.menuBar;
        }
        
        public void add_to_menuBar(String menuName)
        {
            this.menuBar.add(Menus.get(menuName));
        }
        
        public void make_menu(String menuName, JMenu menuObject)
        {
            this.Menus.put(menuName, menuObject);
        }
        
        public void add_menu_item(String menuName, String itemName, JMenuItem menuItem)
        {
            this.Menus.get(menuName).add(menuItem);
            this.MenuItems.put(menuName, itemName);
        }   
    }
    
    public class PanelManager
    {
        private HashMap<String, JPanel> Panels = new HashMap<>();
        
        public void createPanel(String panel_name, JPanel object)
        {
            Panels.put(panel_name, object);
        }
        
        public JPanel accessPanel(String panel_name)
        {
            return Panels.get(panel_name);
        }
        
        
        public HashMap<String, JPanel> accessPanelStore()
        {
            return Panels;
        }
    }
    
    public void test()
    {
        HashMap<String, String> Map = new HashMap<>();
        Map.put("1", "God");
        Map.put("2", "is");
        Map.put("3", "good");
        Map.put("4", "Jesus");
        Map.put("5", "is");
        Map.put("6", "the");
        Map.put("7", "Son");
        Map.put("8", "of");
        Map.put("9", "God");
        
        for (String val : Map.values())
        {
            System.out.print(val);
        }
    }
    
    public DrawingAppDeji_Week1()
    {
        Window window = new Window(1200, 675);
        
        PanelManager panelManager = new PanelManager();
        panelManager.createPanel("canvas_panel", new JPanel());
        panelManager.createPanel("control_panel", new JPanel());
        panelManager.createPanel("message_area_panel", new JPanel());
        
//        JPanel canvasPanel = new JPanel();
//        JPanel controlPanel = new JPanel();
//        JPanel messageAreaPanel = new JPanel();
        
        
//        panelManager.accessPanel("canvas_panel").setBorder(new TitledBorder(new EtchedBorder(), "Canvas"));
//        panelManager.accessPanel("control_panel").setBorder(new TitledBorder(new EtchedBorder(), "Control Panel"));
//        panelManager.accessPanel("message_area_panel").setBorder(new TitledBorder(new EtchedBorder(), "Message Area"));
        
        for (HashMap.Entry<String, JPanel> panelItem : panelManager.accessPanelStore().entrySet())
        {
            String name = panelItem.getKey();
            panelItem.getValue().setPreferredSize(new Dimension(200, 100));
            
            switch(name)
            {
                case "canvas_panel" -> {
                    panelItem.getValue().setBorder(new TitledBorder(new EtchedBorder(), "Canvas"));
                    window.add(panelItem.getValue(), window.border.CENTER);
                }
                
                case "control_panel" -> 
                {
                    panelItem.getValue().setBorder(new TitledBorder(new EtchedBorder(), "Control Panel"));
                    window.add(panelItem.getValue(), window.border.LINE_START);
                }
                
                case "message_area_panel" ->
                {
                    panelItem.getValue().setBorder(new TitledBorder(new EtchedBorder(), "Message Area"));
                    window.add(panelItem.getValue(), window.border.PAGE_END);
                }
//                window.add(controlPanel, window.border.CENTER);
//                window.add(controlPanel, window.border.LINE_START);
//                window.add(messageAreaPanel, window.border.PAGE_END);
            }
        }
        
        
        MenuManager myMenuControl = new MenuManager();
        myMenuControl.make_menu("file_menu", new JMenu("File"));
        myMenuControl.make_menu("help_menu", new JMenu("Help"));
        myMenuControl.add_menu_item("file_menu", "Save", new JMenuItem("Save"));
        myMenuControl.add_menu_item("file_menu", "Load", new JMenuItem("Load"));
        myMenuControl.add_menu_item("file_menu", "Exit", new JMenuItem("Exit"));
        myMenuControl.add_menu_item("help_menu", "About", new JMenuItem("About"));
        myMenuControl.add_to_menuBar("file_menu");
        myMenuControl.add_to_menuBar("help_menu");
        
        
        window.add(myMenuControl.access_menuBar());
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.pack();
        window.setVisible(true);

//        test();
    }
    
    public DrawingAppProject_Deji()
    {
        Window window = new Window(1200, 675);
        
        JPanel canvasPanel = new JPanel();
        JPanel controlPanel = new JPanel();
        JPanel messageAreaPanel = new JPanel();
        
        canvasPanel.setBorder(new TitledBorder(new EtchedBorder(), "Canvas"));
        controlPanel.setBorder(new TitledBorder(new EtchedBorder(), "Canvas"));
        messageAreaPanel.setBorder(new TitledBorder(new EtchedBorder(), "Canvas"));
        
        canvasPanel.setPreferredSize(new Dimension(200, 100));
        controlPanel.setPreferredSize(new Dimension(200, 100));
        messageAreaPanel.setPreferredSize(new Dimension(200, 100));
        
        MenuWrapper myMenuControl = new MenuWrapper();
        myMenuControl.make_menu("file_menu", new JMenu("File"));
        myMenuControl.add_menu_item("file_menu", "Save", new JMenuItem("Save"));
        myMenuControl.add_to_menuBar("file_menu");
        
        
        window.add(canvasPanel, window.border.CENTER);
        window.add(controlPanel, window.border.LINE_START);
        window.add(messageAreaPanel, window.border.PAGE_END);
        
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.pack();
        window.setVisible(true);
    }
            
    
    
    public static void main(String[] args)
    {
        DrawingAppProject_Deji myApp = new DrawingAppProject_Deji();
    }
    
}
