## 要求⼆：建立資料庫和資料表
![2](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/2.png "建立member資料表")

## 要求三：SQL CRUD
● 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。
![3-1](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-1.png "新增test資料")

● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
![3-2](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-2.png "新增4筆資料")

● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![3-3](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-3.png "按time排列")

● 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
![3-4](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-4.png "選取2-4筆資料")

● 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
![3-5](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-5.png "取username=test之資料")

● 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![3-6](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-6.png "取username%password=test之資料")

● 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
![3-7](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/3-7.png "更新test的資料")

## 要求四：SQL Aggregate Functions
● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。  
![4-1](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/4-1.png "count")

● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![4-2](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/4-2.png "sum")

● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![4-3](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/4-3.png "avg")

## 要求五：SQL JOIN (Optional)
![5-1](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/5-1.png "avg")

● 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
![5-2](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/5-2.png "結合資料表")

● 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
![5-3](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/5-3.png "取test為username的資料")

● 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
![5-4](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/5-4.png "平均按讚數")

## 額外
| 欄位名稱 | 用途說明 |
|-------|:-----:|
| mem_id   |  留言按讚者的編號  |
| mesg_id   |  被按讚的留言編號  |  

● 建立whoLike資料表  
![額外-1](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/額外-1.png "平均按讚數")

● 根據留言編號取得該留言有哪些會員按讚
```MySQL
select whoLike.mesg_id, message.content, mem_id, member.name from(whoLike inner join member on whoLike.mem_id = member.id)
inner join message on whoLike.mesg_id = message.id order by mesg_id
```
![額外-2](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/額外-2.png "平均按讚數")

● 檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。
```MySQL
insert into whoLike(mesg_id, mem_id) values(1,1);
```
![額外-3](https://github.com/wanhsuan625/WeHelp_assingment/blob/main/week-5/img/額外-3.png "平均按讚數")
