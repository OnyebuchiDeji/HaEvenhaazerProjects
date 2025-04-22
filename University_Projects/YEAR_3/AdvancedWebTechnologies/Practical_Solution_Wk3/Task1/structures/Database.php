<?php
    class Database{
        //  Database Credentials
        private $m_Host = "katara.scam.keele.ac.uk";
        private $m_Dbname = "x7e30";
        private $m_Username = "x7e30";
        private $m_Password = "x7e30x7e30";

        public $Conn;


        //  Get the database connection
        //  Pree the OOP method of connecting to the database
        public function GetConnection(){
            $this->Conn = null;

            try{
                $this->Conn = new PDO("mysql:host=" . $this->m_Host . ";dbname=" . $this->m_Dbname, $this->m_Username, $this->m_Password);
                $this->Conn->exec("set names utf8");
                echo "Connected to Database: {Host: $this->m_Host, DbName: $this->m_Dbname, User: $this->m_Username} <br><br>";
            }
            catch(PDOException $exceps){
                echo "Connection Error: " . $exceps->getMessage() ."<br><br>";
            }
            return $this->Conn;
        }

    }
?>