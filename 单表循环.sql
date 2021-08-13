SELECT * FROM `t_employees` WHERE deptno = 30
SELECT ename,empno,job FROM `t_employees`
SELECT * FROM `t_employees` WHERE comm > sal
SELECT * FROM `t_employees` WHERE comm > sal * 0.6
SELECT * FROM `t_employees` WHERE job = "经理" AND deptno = 10 OR job = "销售员" AND deptno = 20
SELECT * FROM t_employees WHERE (deptno=10 AND job='经理') OR (deptno=20 AND job='销售员')OR (sal >=20000 AND job!='经理'OR job!='销售员')
SELECT * FROM `t_employees` WHERE comm < 1000 OR comm IS NULL
SELECT * FROM `t_employees` WHERE ename LIKE "___"
SELECT * FROM `t_employees` WHERE hiredate = 2000
SELECT * FROM `t_employees` ORDER BY empno ASC
SELECT * FROM t_employees ORDER BY Sal DESC,hiredate ASC;
SELECT AVG(sal),job FROM `t_employees`GROUP BY job
SELECT COUNT(job),job FROM `t_employees`GROUP BY job
SELECT MAX(sal),MIN(sal),COUNT(job) FROM `t_employees`