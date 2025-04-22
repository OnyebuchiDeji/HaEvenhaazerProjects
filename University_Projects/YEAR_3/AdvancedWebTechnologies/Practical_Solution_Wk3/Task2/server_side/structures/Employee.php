<?php

    class Employee{
        //  Database connection and table name
        private $m_Conn;
        private $m_TableName = "";
        
        //  Object Properties
        public $id;
        public $name;
        public $salary;
        public $age;

        //  Constructor with $db as database connection
        public function __construct($dbConnection, $tableName){
            $this->m_Conn = $dbConnection;
            $this->m_TableName = $tableName;
        }

        function Register()
        {
            if ($this->AlreadyExists()){
                return false;
            }

            //  Insert Query
            $query = "INSERT INTO " . $this->m_TableName . " SET
            employee_name=:name, employee_salary=:salary, employee_age=:age";

            //  Prepare Query for Execution
            $stmnt = $this->m_Conn->prepare($query);

            //  Sanitize Input
            $this->name=htmlspecialchars(strip_tags($this->name));
            $this->salary=htmlspecialchars(strip_tags($this->salary));
            $this->age=htmlspecialchars(strip_tags($this->age));

            //  Bind Values
            //  Cannot do $this->$username
            $stmnt->bindParam(":name", $this->name);
            $stmnt->bindParam(":salary", $this->salary);
            $stmnt->bindParam(":age", $this->age);

            //  Execute Query
            if ($stmnt->execute()){
                //  `lastInsertId` returns the id of the record last inserted
                $this->id = $this->m_Conn->lastInsertId();
                return true;
            }
            return false;
        }

        //  Checks if the employee with 'employee_name' exists
        function AlreadyExists(){
            //  make sure to leave space after the FROM and WHERE
            $query = "SELECT * FROM " . $this->m_TableName . " WHERE
                employee_name='".$this->name."'";
            //  Prepare Query Statement
            $stmnt = $this->m_Conn->prepare($query);
            //  Execute
            $stmnt->execute();
            //  If it exists there should be at least 1 record (row)
            if ($stmnt->rowCount() > 0){
                return true;
            }
            else{
                return false;
            }
        }
    }

?>