# 数据获取
从data_train.txt每行url下载图片，图片命名方式为label__linenumber.jpg

下载代码：

	!/bin/bash

	i=0
	while read LINE
	do
	    let i=$i+1
	    num=${LINE% *}
	    url=${LINE#* }
	    pic_name=$num"_"$i".jpg"
	    file_name=$pic_name
	    if [[ (! -f "./train_data/$file_name") || (! -s "./train_data/$file_name") ]]; then
	        wget $url -O "./train_data/$file_name" -T 5 -t 1
	    fi
	done < 'data_train.txt'
## 数据统计
训练集文件包含8209个url，其中有效url有7626个，各label数量分布如下。

|数量|label|
|---|---|
|96|0|
|91|1|
|93|2|
|98|3|
|92|4|
|94|5|
|87|6|
|36|7|
|93|8|
|34|9|
|39|10|
|23|11|
|91|12|
|25|13|
|48|14|
|38|16|
|91|17|
|97|18|
|95|19|
|35|20|
|95|21|
|79|22|
|95|23|
|92|24|
|95|25|
|96|26|
|31|27|
|94|28|
|94|29|
|93|30|
|91|31|
|48|32|
|97|33|
|94|34|
|42|35|
|98|36|
|97|37|
|92|38|
|93|39|
|46|40|
|29|41|
|98|42|
|44|43|
|37|45|
|77|46|
|73|47|
|93|48|
|94|49|
|99|50|
|92|51|
|93|52|
|61|53|
|96|54|
|66|57|
|97|59|
|92|60|
|94|61|
|96|62|
|62|63|
|84|64|
|93|65|
|91|66|
|84|67|
|95|68|
|96|69|
|38|70|
|92|71|
|80|72|
|60|73|
|52|74|
|79|75|
|83|76|
|97|77|
|61|78|
|36|79|
|95|80|
|90|81|
|57|82|
|39|83|
|49|84|
|50|85|
|28|86|
|96|87|
|86|88|
|22|94|
|93|95|
|31|97|
|93|101|
|84|109|
|93|111|
|95|114|
|99|115|
|85|120|
|91|123|
|96|126|
|94|127|
|96|128|
|94|129|
|92|132|
|30|133|

无效url有583个，http错误有432个，wget错误127个，文件损坏24个，包含以下几种情况。

|数量|错误类型|
|---|---|
|16|200 OK|
|14|301 Moved Permanently|
|2|302 Found|
|15|302 Moved Temporarily|
|24|400 Bad Request|
|104|403 Forbidden|
|208|404 Not Found|
|3|404 Unknown HostName!|
|1|404 Unknown virtual host|
|1|405 Not Allowed|
|1|415 Unsupported Media Type|
|5|502 Bad Gateway|
|12|503 Service Temporarily Unavailable|
|5|503 Service Unavailable|
|3|No data received.|
|14|Read error (Connection reset by peer) in headers.|
|4|Read error (Operation timed out) in headers.|
|127|wget error|