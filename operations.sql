--JOIN Statements
--1. Inner Join
SELECT
    Appointment_556.Start_time as Appointment_time,
    Appointment_556.Appointment_type,
    Patient_556.First_Name as Patient_FirstName,
    Patient_556.Last_Name as Patient_LastName,
    Doctor_556.First_Name as Doctor_FirstName,
    Doctor_556.Last_Name as Doctor_LastName
FROM Patient_556
JOIN Appointment_556
ON Patient_556.Patient_ID = Appointment_556.Patient_ID
JOIN Doctor_556
ON Doctor_556.Doctor_ID = Appointment_556.Doctor_ID;

--2. Natural Join
SELECT
    Patient_556.First_Name as Patient_FirstName,
    Patient_556.Last_Name as Patient_LastName,
    Treatment_556.Medication as Prescribed_Medication
FROM Patient_556
NATURAL JOIN Treatment_556;

--3. Right join
SELECT
    Patient_556.Patient_ID,
    Patient_556.First_Name as Patient,
    Billing_556.Total_amount as Amount_to_be_Paid
FROM Patient_556
RIGHT JOIN Billing_556
ON Patient_556.Patient_ID = Billing_556.Patient_ID
WHERE Billing_556.Payment_Status = 'Pending';

--4. Left Join
SELECT
    distinct concat(First_Name,' ',Last_Name) as Doctor,
    review_556.Review_ID,
    review_556.cleanliness, review_556.Communication, review_556.Professionalism
FROM Doctor_556
LEFT JOIN Treatment_556
ON Treatment_556.Doctor_ID = Doctor_556.Doctor_ID
JOIN Review_556
ON Review_556.Doctor_ID = Doctor_556.Doctor_ID
WHERE Review_556.Cleanliness<=5 AND Review_556.Communication<=8 AND Review_556.Professionalism<=8;

-- -------------------------------------------------------------------------------------------------------------------------------

--Aggregate func
--1. SUM
SELECT
    SUM(Total_amount) as Amount,
    Payment_Status
FROM Billing_556
GROUP BY Payment_Status;

--2. MAX (highest ratings received)
SELECT
    concat(First_Name,' ',Last_Name) as Doctor,
    MAX(review_556.Professionalism),
    MAX(review_556.Communication),
    MAX(review_556.Cleanliness)
FROM Doctor_556
NATURAL JOIN review_556
GROUP BY Doctor_ID;

--3. MIN (least ratings received)
SELECT
    concat(First_Name,' ',Last_Name) as Doctor,
    MIN(review_556.Professionalism),
    MIN(review_556.Communication),
    MIN(review_556.Cleanliness)
FROM Doctor_556
NATURAL JOIN review_556
GROUP BY Doctor_ID;

--4. COUNT (Number of appointments on 2022-11-29 )
SELECT 
    concat(First_Name,' ',Last_Name) as Doctor,
    COUNT(Appointment_556.Appointment_type)
FROM Doctor_556
NATURAL JOIN Appointment_556
WHERE  Date_of_appointment = '2022-11-27'
GROUP BY Doctor_ID;

-- -------------------------------------------------------------------------------------------------------------------------------

--UNION (Patient_ID and their corresponding Doctor_ID's assigned for treatment)
SELECT Patient_ID,Doctor_ID, APPOINTMENT_ID FROM Appointment_556
Where Doctor_ID='D01'
UNION
SELECT Patient_ID,Doctor_ID, APPOINTMENT_ID FROM Treatment_556;

--INTERSECT (Doctor who is also a patient)
SELECT concat(First_Name,' ',Last_Name) as Doctor FROM Doctor_556
INTERSECT
SELECT concat(First_Name,' ',Last_Name) as patient FROM Patient_556;

--MINUS (Which doctor does not work on any patient)
SELECT concat(First_Name,' ',Last_Name) as Doctor 
    FROM Doctor_556
    WHERE Doctor_ID
    IN (SELECT Doctor_ID FROM Doctor_556
        EXCEPT
        SELECT Doctor_ID FROM  Treatment_556);

--MINUS (Which patient has not been assigned an appointment yet)
SELECT Patient_ID, concat(First_Name,' ',Last_Name) as Patient_Name 
    FROM Patient_556 
    WHERE Patient_ID 
    IN (SELECT Patient_ID from Patient_556
        EXCEPT
        SELECT Patient_ID from Appointment_556);

-- -------------------------------------------------------------------------------------------------------------------------------

--Function
DELIMITER $$ 
CREATE FUNCTION needsPedodonntist( 
dob date,
currentdate date
) 
RETURNS VARCHAR(100) 
DETERMINISTIC 
BEGIN 
declare currentdate date;
IF dob > '2008-01-01' THEN 
RETURN ("Is less than 14 years of age, consult a Pedodontist"); 
ELSE 
RETURN ("Is not less than 14 years of age, pedodontic consultation not necessary"); 
END IF; 
END$$ 
DELIMITER $$

--------------------To check if the function is working or not----------------------------------------------------
-- SELECT first_name, last_name, needsPedodonntist(dob,'2022-11-22') as Pedodontist_Requirement from patient_556;

-- -------------------------------------------------------------------------------------------------------------------------------

-- Triggers
delimiter $$
CREATE TRIGGER invalid_phone_number
BEFORE INSERT ON Patient_556
FOR EACH ROW
BEGIN
IF NEW.Phone NOT LIKE '__________%' THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Invalid phone number';
END IF;
END$$
delimiter ;

------------to check the Invalid phone number condition of the trigger----------
-- INSERT INTO patient_556(Address,DOB,Patient_ID,First_name,Last_Name,Gender,Email,Phone)

-- Values('423 QWE','2001-03-22','P14','Deepanjali','Pandit','F','haw@atd',8472738);*/

------------to check the valid condition of the trigger----------
-- INSERT INTO patient_556(Address,DOB,Patient_ID,First_name,Last_Name,Gender,Email,Phone)

-- Values('423 QWE','2001-03-22','P11','Deepanjali','Pandit','F','haw@atd',8472738901);
-------------------------------------------------------------------------------------------------------------------------------------

--Procedure
DELIMITER $$
CREATE PROCEDURE getPatientInfo()
BEGIN
    SELECT * FROM Patient_556 WHERE dob > '2008-01-01';
    SELECT COUNT(*) as Total_Patients FROM Patient_556 WHERE dob > '2008-01-01';
END$$
DELIMITER $$

-- call getPatientInfo $$

-------------------------------------------------------------------------------------------------------------------------------------

--cursor
delimiter $$
create procedure concat_NameSalary()
begin
    declare v_first_name varchar(20);
    declare v_last_name varchar(20);
    declare v_annual_salary int;
    declare v_done integer default 0;
    declare c1 cursor for select first_name,last_name, annual_salary from doctor_556;
    declare continue handler for not found set v_done = 1;
    open c1;
    read_loop: loop
        fetch c1 into v_first_name, v_last_name, v_annual_salary;
        if v_done=1 then
            leave read_loop;
        end if;
        select concat(v_first_name,' ',v_last_name) as Doc_Name , v_annual_salary;
    end loop read_loop;
    close c1;
end$$

-- call concat_NameSalary(); $$

-------------------------------------------------------------------------------------------------------------------------------------

--Run Query to get the result in Run Page

INSERT INTO  patient_556(Address,DOB,Patient_ID,First_name,Last_Name,Gender,Email,Phone)  Values('74D WDE' , '2009-05-11' , 'P45' , 'veer' , 'Pandit' , 'M' , 'noob@atd' , 9472738645);