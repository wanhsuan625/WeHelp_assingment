window.onload=getData()
function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
            return response.json();
        }).then(function(data){
            let jsonObj = data["result"]["results"];
            // console.log(jsonObj[i].stitle);
            // console.log(jsonObj[i].file.split("https://"));          # [0]是空值
            // console.log(jsonObj[i].file.split("https://")[1]);

        // 上面的兩個
            for(let i = 0; i < 2; i++){
                let pic = "https://" + jsonObj[i].file.split("https://")[1];     // 圖片網址
                let viewName = jsonObj[i].stitle;      // 景點名稱
                let div_imgbox = document.querySelectorAll(".imgBox");  // 圖片父層
                let div_title = document.querySelectorAll(".title");    // 文字父層

                // 抓圖片 img
                let title_img = document.createElement("img");
                title_img.setAttribute('src', pic);
                div_imgbox[i].appendChild(title_img);

                // 抓景點名
                let prom = document.createElement("div");
                prom.setAttribute('class', "prom");
                prom.textContent = viewName;
                div_title[i].appendChild(prom);
            }

        // 下面的八個
            jsonObj.splice(0, 2);  // 因為要從0開始，所以先刪掉前兩張用過的
            for(let j = 0; j < 8; j++){
                let pic = "https://" + jsonObj[j].file.split("https://")[1];     // 圖片網址
                let viewName = jsonObj[j].stitle;      // 景點名稱
                let div_imgbox = document.querySelectorAll(".cardImgBox");  // 圖片父層
                let div_card = document.querySelectorAll(".card");    // 文字父層

                // 抓圖片 img
                let card_img = document.createElement("img");
                card_img.setAttribute('src', pic);
                div_imgbox[j].appendChild(card_img);

                // 抓景點名
                let card = document.createElement("div");
                card.setAttribute('class', "word");
                card.textContent = viewName;
                div_card[j].appendChild(card);
            }   
    })
}  