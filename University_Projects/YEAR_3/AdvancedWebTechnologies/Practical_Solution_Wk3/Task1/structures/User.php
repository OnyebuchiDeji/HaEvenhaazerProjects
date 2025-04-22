<?php

    class User{
        //  Database connection and table name
        private $m_Conn;
        private $m_TableName = "";
        
        //  Object Properties
        public $id;
        public $username;
        public $password;
        public $created;

        //  Constructor with $db as database connection
        public function __construct($dbConnection, $tableName){
            $this->m_Conn = $dbConnection;
            $this->m_TableName = $tableName;
        }
        //  Signup User
        /**
         *  Basically, if the user already exists, signup does not continue so return false.
         *  But if the user doesn't, save their info into the database
         *  and return true to show success.
         */
        function SignUp(){
            if ($this->AlreadyExists()){
                return false;
            }
            //  query to insert record
            //  Note the ':username', ':password', ':created'
            //  they are place holder strings that are replaced with the corresponding real value
            //  by the `bindParam` function.
            //  make sure to leave space after the INTO and SET
            $query = "INSERT INTO " . $this->m_TableName . " SET
                 username=:username, password=:password, created=:created";

            //  Prepare Query for Execution
            $stmnt = $this->m_Conn->prepare($query);

            //  Sanitize Input
            $this->username=htmlspecialchars(strip_tags($this->username));
            $this->password=htmlspecialchars(strip_tags($this->password));
            $this->created=htmlspecialchars(strip_tags($this->created));

            //  Bind Values
            //  Cannot do $this->$username
            $stmnt->bindParam(":username", $this->username);
            $stmnt->bindParam(":password", $this->password);
            $stmnt->bindParam(":created", $this->created);

            //  Execute Query
            if ($stmnt->execute()){
                //  `lastInsertId` returns the id of the record last inserted
                $this->id = $this->m_Conn->lastInsertId();
                return true;
            }
            return false;
        }

        //  Login User
        function Login(){
            //  Select All Query
            /**
             *  The below query gets all field data for the user with that password
             *  and username
             */
            //  make sure to leave space after the FROM and WHERE
            $query = "SELECT `id`, `username`, `password`, `created`
                FROM " . $this->m_TableName . " WHERE username='".$this->username."'
                 AND password='".$this->password."'";
            
            //  Prepare Query for Execution
            $stmnt = $this->m_Conn->prepare($query);
            //  Execute
            $stmnt->execute();
            return $stmnt;
        }

        //  Checks if the user wirh 'username' exists
        function AlreadyExists(){
            //  make sure to leave space after the FROM and WHERE
            $query = "SELECT * FROM " . $this->m_TableName . " WHERE
                username='".$this->username."'";
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