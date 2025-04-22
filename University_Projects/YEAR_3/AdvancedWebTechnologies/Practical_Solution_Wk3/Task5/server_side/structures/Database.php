<?php
    class Database{
        //  Database Credentials
        private $m_Host = "katara.scam.keele.ac.uk";
        private $m_Dbname = "x7e30";
        private $m_Username = "x7e30";
        private $m_Password = "x7e30x7e30";

        public $Conn;

        public function __construct()
        {
            $this->InitConnection();
        }

        //  Get the database connection
        //  Pree the OOP method of connecting to the database
        public function InitConnection(){
            $this->Conn = null;

            try{
                $this->Conn = new PDO("mysql:host=" . $this->m_Host . ";dbname=" . $this->m_Dbname, $this->m_Username, $this->m_Password);
                $this->Conn->exec("set names utf8");
                echo "<br><br>Connected to Database: {Host: $this->m_Host, DbName: $this->m_Dbname, User: $this->m_Username} <br><br>";
            }
            catch(PDOException $exceps){
                echo "<br><br>Connection Error: " . $exceps->getMessage() ."<br><br>";
            }
            return $this->Conn;
        }

        public function GetConnection(){
            return $this->Conn;
        }

        public function GetAllRecords($tableName){
            $tableName=htmlspecialchars(strip_tags($tableName));
            $query = "SELECT * FROM " . $tableName;

            //  Prepare statement for execution
            $stmnt = $this->Conn->prepare($query);
            //  Execute Query
            $stmnt->execute();
            return $stmnt;
        }

        public function DeleteRecord($tableName, $id){
            $tableName=htmlspecialchars(strip_tags($tableName));
            $id=htmlspecialchars(strip_tags($id));

            $query = "delete from " . $tableName . " where id = '".$id."'";
            $statement = $this->Conn->prepare($query);
            if ($statement->execute())
            {
                $data[] = array(
                    'success' => true,
                    "message" => "Record of id $id deleted successfully.",
                );
                return $data;
            }
            $data[] = array(
                'success' => false,
                "message"=>"Record of id $id could not be found and deleted.",
            );
        }

        public function UpdateRecord($tableName, $id, $newData){

            $tableName=htmlspecialchars(strip_tags($tableName));
            $id=htmlspecialchars(strip_tags($id));
            $newData['employeeName'] = htmlspecialchars(strip_tags($newData['employeeName']));
            $newData['employeeSalary'] = htmlspecialchars(strip_tags($newData['employeeSalary']));
            $newData['employeeAge'] = htmlspecialchars(strip_tags($newData['employeeAge']));
            $newData['id'] = $id;

            $query = "
                update $tableName 
                set employee_name=:employeeName, employee_salary=:employeeSalary,
                    employee_age=:employeeAge
                where id=:id
                ";
            $statement = $this->Conn->prepare($query);
            if ($statement->execute($newData))
            {
                $data[] = array(
                    'success' => true,
                    "message" => "Record of id $id updated successfully.",
                );
                return $data;
            }
            
            $data[] = array(
                'success' => false,
                "message"=>"Record of id $id could not be found and updated.",
            );

            return $data;
        }
    }
?>