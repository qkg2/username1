<?php

$token = "6015809423:AAHzyrNvpLVwDoFlyKyc5ajewgzeZOyvuZc";
$Df = "5099564264";
 define('API_KEY',$token);
echo file_get_contents("https://api.telegram.org/bot" . API_KEY . "/setwebhook?url=" . $_SERVER['SERVER_NAME'] . "" . $_SERVER['SCRIPT_NAME']);
            function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}

mkdir("data");
$name_tag = "[$name](tg://user?id=$from_id)";

$update = json_decode(file_get_contents('php://input'));
if($update->message){
	$message = $update->message;
$message_id = $update->message->message_id;
$username = $message->from->username;
$chat_id = $message->chat->id;
$title = $message->chat->title;
$text = $message->text;
$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
}
if($update->callback_query){
$data = $update->callback_query->data;
$chat_id = $update->callback_query->message->chat->id;
$title = $update->callback_query->message->chat->title;
$message_id = $update->callback_query->message->message_id;
$name = $update->callback_query->message->chat->first_name;
$user = $update->callback_query->message->chat->username;
$from_id = $update->callback_query->from->id;
}
if($update->edited_message){
	$message = $update->edited_message;
	$message_id = $message->message_id;
$username = $message->from->username;
$chat_id = $message->chat->id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
	}
	if($update->channel_post){
	$message = $update->channel_post;
	$message_id = $message->message_id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->chat->username;
$title = $message->chat->title;
$name = $message->author_signature;
$from_id = $message->chat->id;
	}
	if($update->edited_channel_post){
	$message = $update->edited_channel_post;
	$message_id = $message->message_id;
$chat_id = $message->chat->id;
$text = $message->text;
$user = $message->chat->username;
$name = $message->author_signature;
$from_id = $message->chat->id;
	}
	if($update->inline_query){
		$inline = $update->inline_query;
		$message = $inline;
		$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
$query = $message->query;
$text = $query;
		}
	if($update->chosen_inline_result){
		$message = $update->chosen_inline_result;
		$user = $message->from->username;
$name = $message->from->first_name;
$from_id = $message->from->id;
$inline_message_id = $message->inline_message_id;
$message_id = $inline_message_id;
$text = $message->query;
$query = $text;
		}
		$tc = $update->message->chat->type;
		$re = $update->message->reply_to_message;
		$re_id = $update->message->reply_to_message->from->id;
$re_user = $update->message->reply_to_message->from->username;
$re_name = $update->message->reply_to_message->from->first_name;
$re_messagid = $update->message->reply_to_message->message_id;
$re_chatid = $update->message->reply_to_message->chat->id;
$photo = $message->photo;
$video = $message->video;
$sticker = $message->sticker;
$file = $message->document;
$audio = $message->audio;
$mmur = file_get_contents("murt.txt");
$mmurt = file_get_contents("channel.txt");
$voice = $message->voice;
$caption = $message->caption;
$photo_id = $message->photo[back]->file_id;
$video_id= $message->video->file_id;
$sticker_id = $message->sticker->file_id;
$file_id = $message->document->file_id;
$music_id = $message->audio->file_id;
$forward = $message->forward_from_chat;
$forward_id = $message->forward_from_chat->id;
$title = $message->chat->title;
if($re){
	$forward_type = $re->forward_from->type;
$forward_name = $re->forward_from->first_name;
$forward_user = $re->forward_from->username;
	}else{
$forward_type = $message->forward_from->type;
$forward_name = $message->forward_from->first_name;
$forward_user = $message->forward_from->username;
$forward_id = $message->forward_from->id;
if($forward_name == null){
	$forward = $message->forward_from_chat;
$forward_id = $message->forward_from_chat->id;
$forward_title = $message->forward_from_chat->title;
	}
}
$title = $message->chat->title;

$carlos = json_decode(file_get_contents("data/carlos.json"),true);
$meca = json_decode(file_get_contents("data/members.json"),true);
$em = json_decode(file_get_contents("data/em.json"),true);
$iinfo = json_decode(file_get_contents("$web"),true);
if($carlos['gch'] == null){
$carlos['gch'] = "❎";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($carlos['d6'] == null){
$carlos['d6'] = "❎";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($carlos['bot'] == null){
$carlos['bot'] = "✅";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($carlos['d7'] == null){
$carlos['d7'] = "❎";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($iinfo['namezar'] == null){
$namezar = "𝗦𝘂𝗿𝘀 𝗫!𝗠𝗮𝘅";
}elseif($iinfo['namezar'] != null){
$namezar = $iinfo['namezar'];
}
if($iinfo['urlzar'] == null){
$urlzar = "https://t.me/OC_C3";
}elseif($iinfo['urlzar'] != null){
$urlzar = $iinfo['urlzar'];
}
$xch = $carlos['ch'];
$xcch = $carlos['cch'];

$members = $meca['members'];
$groups = $meca['group'];
$id_admin = $carlos['admin'];
$md3 = count($meca['members']);
$md5 = count($meca['group']);
$countall = $md5 + $md3;
$md4 = count($meca['banbots']) - 1;
if($tc == 'private' and !in_array($from_id,$members)){
$meca['members'][] = $from_id;
file_put_contents("data/members.json",json_encode($meca,32|128|265));
}
$addgroup = bot('getchatmemberscount',['chat_id'=>$chat_id])->result;
$namegroup = $update->message->chat->title;
if($text and !in_array($chat_id,$groups)){
if($tc != 'private'){
bot('sendmessage',[
'chat_id'=>$Df,
'text'=>"
*‹ : تم تفعيل مجموعه جديده *
*‹ : من قام بتفعيلها :* $name 
*‹ : معلومات المجموعه :*
*‹ : الاسم :* $namegroup
*‹ : عدد الاعضاء :* $addgroup
*‹ : جميع الاحصائيات :* $countall
",
'parse_mode'=>"Markdown",
]);
$meca['group'][] = $chat_id;
file_put_contents("data/members.json",json_encode($meca,32|128|265));
}
}
$idleft = $update->message->left_chat_member->id;
$idbot = bot('getme',['d'])->result->id;
if($update->message->left_chat_member and $idleft==$idbot){
bot('sendMessage',[
'chat_id'=>$Df,
'text'=>"*‹ :  تم طرد البوت من مجموعه جديده *
*‹ :  اسم المجموعه :* $namegroup
*‹ :  ايدي المجموعه :* $chat_id
*‹ :  تم مسح جميع البيانات المتعلقه بالمجموعه*",
'parse_mode'=>"MarkDown",
]);
$key = array_search($chat_id,$meca["group"]);
unset($meca["group"][$key]);
$meca["group"] = array_values($meca["group"]); 
$meca = json_encode($meca,true);
file_put_contents("data/members.json",$meca);
}
$dd = date('D');
$em1 = count($em[$dd]);
$em2 = $em[$dd];
if($message and !in_array($from_id, $em2)){ 
$em[$dd][] = $from_id;
file_put_contents("data/em.json",json_encode($em,32|128|265));
}
if(!$carlos['sudo']){
$iidsod = $Df;
}elseif($carlos['sudo']){
$iidsod = $carlos['sudo'];
}
$admin = $iidsod;

$tag_name = "[$name](tg://user?id=$from_id)";
if($carlos['start'] == null){
$start = "

";
}elseif($carlos['start'] != null){
$start = $carlos['start'];
}
$XQ_3X = [
"start"=>$start,
"admin"=>"
━━━━━━━━━━━━━━━━━━━━━━━━
                     『 بوت تمويل  』           
━━━━━━━━━━━━━━━━━━━━━━━━
اهلا بك 🎭 عزيزي الادمن 🍿 هذه لوحة التحكم الخاصة بك 🥡 اختر ما تريد ...
━━━━━━━━━━━━━━━━━━━━━━━━
🎟️ : قناتي 
@AFTU2
━━━━━━━━━━━━━━━━━━━━━━━━
",
"off"=>"- عذرأ عزيزي حاليأ البوت معطل لتحديث جديدة..🔍",
"ban"=>"⚠️- *عذرأ عزيزي لقد قام المطور بحظرك من هاذ البوت*",
"sand"=>"
• مرحبا بك في قسم الاذاعه 🔥

• عدد المسخدمين الكلي : $countall
- عدد الخاص بك : $countall
- عدد الكروبات والقنوات : $md5

- عدد المحظورين : $addbanlst
",
"sand1"=>"".$klisaamr."*أرسل رسالتك وسيتم إرسالها لـ $md3 من الاعضاء .*",
"sand2"=>"".$klisaamr."*تم ارسأل رسالتك لـ $md3 من الاعضاء .*",
"sand3"=>"".$klisaamr."*ارسأل رسالتك وسيتم ارسالها لـ $md5 من الكروبات .*",
"sand4"=>"".$klisaamr."*تم ارسأل رسالتك لـ $md5 من الكروبات .*",
"sand5"=>"".$klisaamr."*ارسأل رسالتك وسيتم ارسالها لـ $countall من الاعضاء و الكروبات .*",
"sand6"=>"".$klisaamr."*تم ارسأل رسالتك لـ $countall من الاعضاء و الكروبات .*",
"sand7"=>"".$klisaamr."*ارسأل رسالتك وسيتم توجيه لـ $countall من الاعضاء و الكروبات .*",
"sand8"=>"".$klisaamr."*تم توجيه رسالتك لـ $countall من الاعضاء و الكروبات .*",
"sand9"=>"".$klisaamr."*أرسل رسالتك وسيتم توجيه لـ $md3 من الاعضاء .*",
"sand10"=>"".$klisaamr."*تم توجيه رسالتك لـ $md3 من الاعضاء .*",
"sand11"=>"".$klisaamr."*ارسأل رسالتك وسيتم توجيه لـ $md5 من الكروبات .*",
"sand12"=>"".$klisaamr."*تم توجيه رسالتك لـ $md5 من الكروبات .*"
];

if($message and $carlos['bot'] == "❎" and $from_id != $admin){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>$XQ_3X["off"]
,'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
exit();
}
if($message and $text != "/start" and $from_id != $admin and $carlos['d7'] == "✅" and !$data and !in_array($from_id,$carlos['ban'])){
bot('forwardMessage',[
'chat_id'=>$admin,
'from_chat_id'=>$chat_id,
 'message_id'=>$update->message->message_id,
'text'=>$text,
]);
}
if($user == null){
$user = "None";
}elseif($user != null){
$user = "[@$user]";
}
if($text == "/start" and $from_id != $admin and $carlos['d6'] == "✅" and !in_array($from_id,$members) and !in_array($from_id,$carlos['ban'])){
bot('sendmessage',[
'chat_id'=>$admin,
'text'=>"
تم دخول عضو جديد الى البوت :
الاسم : [$name]
المعرف : $user
الايدي : [$from_id](tg://user?id=$from_id)
⎯ ⎯ ⎯ ⎯
عدد المستخدمين : $md3
",
'parse_mode'=>"Markdown",
]);
}

$ch11 = $carlos['ch1'];
$ch1 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$ch11."&user_id=".$from_id);
if($message && (strpos($ch1,'"status":"left"') or strpos($ch1,'"Bad Request: USER_ID_INVALID"') or strpos($ch1,'"status":"kicked"'))!== false){
	if($tc == "private"){
$a = str_replace("@","",$carlos['ch1']);
$get = file_get_contents("http://api.telegram.org/bot".API_KEY."/getChat?chat_id=".$carlos['ch1']); 
$js = json_decode($get); 
$res = $js->result;
$namech = $res->title; 
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"
- عذراً عزيزي 
- يجب عليك الاشتراك في قنوات البوت أولا ✅
- اشترك ثم ارسل /start ⬇️
[$namech](t.me/$a)
"
,'reply_to_message_id'=>$message->message_id,"parse_mode"=>"MarkDown","disable_web_page_preview"=>true,'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"اشتراك ",'url'=>"https://t.me/$a"]],
]
])
]);return false;
}
}
$ch22 = $carlos['ch2'];
$ch2 = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$ch22."&user_id=".$from_id);
if($message && (strpos($ch2,'"status":"left"') or strpos($ch2,'"Bad Request: USER_ID_INVALID"') or strpos($ch2,'"status":"kicked"'))!== false){
if($tc == "private"){
$get = file_get_contents("http://api.telegram.org/bot".API_KEY."/getChat?chat_id=".$carlos['ch2']); 
$js = json_decode($get); 
$res = $js->result;
$namech = $res->title; 
$a = str_replace("@","",$carlos['ch2']);
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"
- عذراً عزيزي 
- يجب عليك الاشتراك في قنوات البوت أولا ✅
- اشترك ثم ارسل /start ⬇️
[$namech](t.me/$a)
"
,"parse_mode"=>"MarkDown","disable_web_page_preview"=>true,'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"اشتراك ",'url'=>"https://t.me/$a"]],
]
])
]);return false;
}
}
$ch111 = $carlos['ch1p'];
$ch222 = $carlos['ch2p'];
$chp = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$ch111."&user_id=".$from_id);
$ch2p = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=".$ch222."&user_id=".$from_id);
if($message && (strpos($chp,'"status":"left"') or strpos($chp,'"status":"kicked"') or strpos($chp,'"Bad Request: USER_ID_INVALID"'))!== false){
if($tc == "private"){
$get = file_get_contents("http://api.telegram.org/bot".API_KEY."/getChat?chat_id=".$carlos['ch1p']); 
$js = json_decode($get); 
$res = $js->result;
$namech = $res->title; 
$chi = $carlos['ch1pp'];
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"
- عذراً عزيزي 
- يجب عليك الاشتراك في قنوات البوت أولا ✅
- اشترك ثم ارسل /start ⬇️
[$namech](t.me/$chi)

",
'parse_mode'=>"MarkDown",
"disable_web_page_preview"=>true,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"اشتراك ",'url'=>"https://t.me/$chi"]],
]
])
]);return false;
}
}
if($message && (strpos($ch2p,'"status":"kicked"') or strpos($ch2p,'"status":"left"') or strpos($ch2p,'"Bad Request: USER_ID_INVALID"') or strpos($ch2p,'"status":"kicked"'))!== false){
if($tc == "private"){
$get = file_get_contents("http://api.telegram.org/bot".API_KEY."/getChat?chat_id=".$carlos['ch2p']); 
$js = json_decode($get); 
$res = $js->result;
$namech = $res->title; 
$chi = $carlos['ch2pp'];
bot('sendMessage', [
'chat_id'=>$chat_id,
'text'=>"
- عذراً عزيزي 
- يجب عليك الاشتراك في قنوات البوت أولا ✅
- اشترك ثم ارسل /start ⬇️
[$namech](t.me/$chi)
"
,"parse_mode"=>"MarkDown","disable_web_page_preview"=>true,'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"اشتراك ",'url'=>"https://t.me/$chi"]],
]
])
]);return false;
}
}

if ($message && in_array($from_id,$carlos['ban'])){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>$XQ_3X["ban"],
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
exit();
}

$ban_id = $message->reply_to_message->forward_from->id;
if($ban_id && $text == "حظر"){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$ban_id"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>" 
- تم حظره بنجاح ✅
",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
$carlos['ban'][] = "$ban_id";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if ($ban_id && $text == "الغاء حظر"){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$ban_id"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
- تم الغاء حظر بنجاح ✅
",
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
]);
$key = array_search($ban_id,$carlos["ban"]);
unset($carlos["ban"][$key]);
$carlos["ban"] = array_values($carlos["ban"]); 
$carlos = json_encode($carlos,true);
file_put_contents("data/carlos.json",$carlos);
}
}

$n = count($json['nas']);

$ahs = "ههه";
$cahadd = "الاشتراك الاجباري";
$staadd = "رساله الترحيب (start)";
$admadd = "قسم الادمنية";
$naadd = "قسم الاذاعه";
$nsadd = "بياناتك ";
$banamradd = "الاحصائيات";

$d6 = $carlos['d6'];
$d7 = $carlos['d7'];
$bot2 = $carlos['bot'];

if($text == "/start"){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
	$d6 = $carlos['d6'];
$d7 = $carlos['d7'];
$bot2 = $carlos['bot'];
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>$XQ_3X["admin"],
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'البوت '.$bot2.'' ,'callback_data'=>"bot3"],['text'=>'الاشعارات '.$d6.'' ,'callback_data'=>"d6"]],
[['text'=>"الردود",'callback_data'=>"redd"],['text'=>"تعديل الازرار",'callback_data'=>"zrar"],['text'=>'التوجية '.$d7.'' ,'callback_data'=>"d7"]],
[['text'=>$staadd,'callback_data'=>"4"]],
[['text'=>$nsadd,'callback_data'=>"Open"],['text'=>'نقل الملكية','callback_data'=>"AddAdmin"]],
[['text'=>$naadd,'callback_data'=>"10"],['text'=>$cahadd,'callback_data'=>"All Ch"]],
[['text'=>$banamradd,'callback_data'=>"lastban"],['text'=>$admadd,'callback_data'=>"5"]],
[["text" => "🧾 اعدادات البوت من هنا 🧾", "callback_data" => "bbuuii"]],
]])
]);
}
}

if($data == "back"){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["admin"],
'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'البوت '.$bot2.'' ,'callback_data'=>"bot3"],['text'=>'الاشعارات '.$d6.'' ,'callback_data'=>"d6"]],
[['text'=>"الردود",'callback_data'=>"redd"],['text'=>"تعديل الازرار",'callback_data'=>"zrar"],['text'=>'التوجية '.$d7.'' ,'callback_data'=>"d7"]],
[['text'=>$staadd,'callback_data'=>"4"]],
[['text'=>$nsadd,'callback_data'=>"Open"],['text'=>'نقل الملكية','callback_data'=>"AddAdmin"]],
[['text'=>$naadd,'callback_data'=>"10"],['text'=>$cahadd,'callback_data'=>"All Ch"]],
[['text'=>$banamradd,'callback_data'=>"lastban"],['text'=>$admadd,'callback_data'=>"5"]],
[["text" => "🧾 اعدادات البوت من هنا 🧾", "callback_data" => "bbuuii"]],
]])
]);
$carlos['addfiles'] = "off";
$carlos['Openstengs'] = "off";
$carlos['ok'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if($data == "d6" ){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
if($carlos['d6']!="✅"){
$dp = "✅";
}else{
$dp ="❎";
}
$carlos['d6'] = $dp;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
$d6 = $carlos['d6'];
$d7 = $carlos['d7'];
$bot2 = $carlos['bot'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'البوت '.$bot2.'' ,'callback_data'=>"bot3"],['text'=>'الاشعارات '.$d6.'' ,'callback_data'=>"d6"]],
[['text'=>"الردود",'callback_data'=>"redd"],['text'=>"تعديل الازرار",'callback_data'=>"zrar"],['text'=>'التوجية '.$d7.'' ,'callback_data'=>"d7"]],
[['text'=>$staadd,'callback_data'=>"4"]],
[['text'=>$nsadd,'callback_data'=>"Open"],['text'=>'نقل الملكية','callback_data'=>"AddAdmin"]],
[['text'=>$naadd,'callback_data'=>"10"],['text'=>$cahadd,'callback_data'=>"All Ch"]],
[['text'=>$banamradd,'callback_data'=>"lastban"],['text'=>$admadd,'callback_data'=>"5"]],
[["text" => "🧾 اعدادات البوت من هنا 🧾", "callback_data" => "bbuuii"]],
]])
]);
}
}
if($data == "d7" ){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
if($carlos['d7']!="✅"){
$as = "✅";
}else{
$as ="❎";
}
$carlos['d7'] = $as;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
$d6 = $carlos['d6'];
$d7 = $carlos['d7'];
$bot2 = $carlos['bot'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'البوت '.$bot2.'' ,'callback_data'=>"bot3"],['text'=>'الاشعارات '.$d6.'' ,'callback_data'=>"d6"]],
[['text'=>"الردود",'callback_data'=>"redd"],['text'=>"تعديل الازرار",'callback_data'=>"zrar"],['text'=>'التوجية '.$d7.'' ,'callback_data'=>"d7"]],
[['text'=>$staadd,'callback_data'=>"4"]],
[['text'=>$nsadd,'callback_data'=>"Open"],['text'=>'نقل الملكية','callback_data'=>"AddAdmin"]],
[['text'=>$naadd,'callback_data'=>"10"],['text'=>$cahadd,'callback_data'=>"All Ch"]],
[['text'=>$banamradd,'callback_data'=>"lastban"],['text'=>$admadd,'callback_data'=>"5"]],
[["text" => "🧾 اعدادات البوت من هنا 🧾", "callback_data" => "bbuuii"]],
]])
]);
}
}
if($data == "bot3" ){
if (in_array($from_id,$id_admin) or $from_id == $admin) {
if($carlos['bot']!="✅"){
$bot = "✅";
}else{
$bot ="❎";
}
$carlos['bot'] = $bot;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
$d6 = $carlos['d6'];
$d7 = $carlos['d7'];
$bot2 = $carlos['bot'];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'البوت '.$bot2.'' ,'callback_data'=>"bot3"],['text'=>'الاشعارات '.$d6.'' ,'callback_data'=>"d6"]],
[['text'=>"الردود",'callback_data'=>"redd"],['text'=>"تعديل الازرار",'callback_data'=>"zrar"],['text'=>'التوجية '.$d7.'' ,'callback_data'=>"d7"]],
[['text'=>$staadd,'callback_data'=>"4"]],
[['text'=>$nsadd,'callback_data'=>"Open"],['text'=>'نقل الملكية','callback_data'=>"AddAdmin"]],
[['text'=>$naadd,'callback_data'=>"10"],['text'=>$cahadd,'callback_data'=>"All Ch"]],
[['text'=>$banamradd,'callback_data'=>"lastban"],['text'=>$admadd,'callback_data'=>"5"]],
[["text" => "🧾 اعدادات البوت من هنا 🧾", "callback_data" => "bbuuii"]],
]])
]);
}
}

if($data == "AddAdmin"){
if ($from_id == $admin) {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"• ارسل الان ايدي المطور الجديد 🧑‍🚀",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "Addadmin";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if(preg_match("/[0-9]/i",$text)){
if($carlos['data'] == "Addadmin" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>" • تمت رفع المطور ✅",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
bot("sendmessage",[
"chat_id"=>$text,
"text"=>"• تم نقل الملكيه البوت الك بنجاح ✅",
]);
$carlos['sudo'] = "$text";
unset($carlos['data']);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}}
if($data == "All Ch"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'🤖اهلا بك في قسم الاشتراك الاجباري ',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'قناه 1' ,'callback_data'=>"AddCh1"],['text'=>'🗑' ,'callback_data'=>"OKDelCh1"]],
[['text'=>'قناه 2' ,'callback_data'=>"AddCh2"],['text'=>'🗑' ,'callback_data'=>"OKDelCh2"]],
[['text'=>' عرض القنوات  ⚙️' ,'callback_data'=>"ALLCH"]],
[['text'=>' رجوع ' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "AddCh1p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'• ارسل ايدي القناه ..!',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'🔙' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "okch1p";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "addp1" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"
تم الحفظ بنجاح ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch1pp'] = "$text";
$carlos['data'] = "stop";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "okch1p" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>" تم اضافه القناة
• قم بأرسال رابط القناة الخاصة..",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch1p'] = "$text";
$carlos['data'] = "addp1";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "DelCh1p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'هل أنت متأكد من أنك تريد حذف القناة ',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'الغاء', 'callback_data'=>'back'],['text'=>'نعم','callback_data'=>'OKDelCh1p']],
]])
]);
}
if($data == "OKDelCh1p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'تم حذف القناة الاولى من الإشتراك الإجباري',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
️[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
unset($carlos['ch1p']);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "AddCh2p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'• ارسل ايدي القناه ..! ',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "okch2p";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "setaddp" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"تم حفظ القناه ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch2pp'] = "$text";
$carlos['data'] = "stop";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "okch2p" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"تم اضافه القناة 
• قم بأرسال رابط القناة الخاصة..",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch2p'] = "$text";
$carlos['data'] = "setaddp";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "DelCh2p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'هل أنت متأكد من أنك تريد حذف القناة ',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'الغاء', 'callback_data'=>'back'],['text'=>'تأكيد','callback_data'=>'OKDelCh2p']],
]])
]);
}
if($data == "OKDelCh2p"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'تم حذف القناة الاولى من الإشتراك الإجباري',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
unset($carlos['ch2p']);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "ALLCHp"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"🔍هذه قائمة القنوات الأشتراك الاجباري 
• القناة الاولى ".$carlos['ch1p']."
• القناة الثانية  ".$carlos['ch2p'],
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع • ' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "AddCh1"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>' 
• قم برفع البوت ادمن في قناتك او مجموعتك اولا 🤍

• من ثم ارسال معرف  قناتك  الى البوت',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "okch1";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "okch1" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"تم حفظ بنجاح ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch1'] = "$text";
$carlos['data'] = "stop";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "DelCh1"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'هل أنت متأكد من أنك تريد حذف القناة ',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'لا', 'callback_data'=>'back'],['text'=>'نعم ','callback_data'=>'OKDelCh1']],
]])
]);
}
if($data == "OKDelCh1"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>' • تم حذف القناه بنجاح ✅ ',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
️[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
unset($carlos['ch1']);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}

if($data == "AddCh2"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'
• قم برفع البوت ادمن في قناتك او مجموعتك اولا 🤍

• من ثم ارسال معرف  قناتك  الى البوت',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "okch2";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data'] == "okch2" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>"تم حفظ بنجاح ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ch2'] = "$text";
$carlos['data'] = "stop";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "DelCh2"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'هل أنت متأكد من أنك تريد حذف القناة ',
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'الغاء', 'callback_data'=>'back'],['text'=>'تاكيد','callback_data'=>'OKDelCh2']],
]])
]);
}
if($data == "OKDelCh2"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>'• تم حذف القناه بنجاح ✅',
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
unset($carlos['ch2']);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "ALLCH"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>" هذه قائمة القنوات الأشتراك الاجباري ⚙️
• القناة الاولى ".$carlos['ch1']."
• القناة الثانية  ".$carlos['ch2'],
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
}

$addbanlst = count($carlos['ban']);
if($data == "lastban"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
مرحبا بك في قسم الاحصائيات 📊

• عدد المسخدمين الكلي : $countall
- عدد الخاص بك : $countall
- عدد الكروبات والقنوات : $md5

• عدد المحظورين : $addbanlst

• عدد المتفاعلين اليوم : $em1
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'المحظورين ( '.$addbanlst.' )' ,'callback_data'=>"##"]],
[['text'=>'حظر' ,'callback_data'=>"bannambar"],['text'=>'الغاء حظر' ,'callback_data'=>"unbannambar"]],
[['text'=>'عرض المحظورين' ,'callback_data'=>"lstesban"],['text'=>'مسح المحظورين' ,'callback_data'=>"dellastban"]],
[['text'=>'قسم الاذاعه ' ,'callback_data'=>"10"]],
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['okunban'] = "done";
$carlos['okban'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "lstesban" and $carlos['ban'] != null){
$banlast = $carlos['ban'];
for($z = 0;$z <= count($banlast)-1;$z++){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$banlast[$z]"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
$result = $result."- [$banname](https://t.me/$banuser) - $banid"."\n";
}
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
اليك قائمة المحظورين : 
$result",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lastban"]],
]])
]);
exit();
}
if($data == "lstesban" and $carlos['ban'] == null){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"لايوجد محظور ",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lastban"]],
]])
]);
}
if($data == "dellastban"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"تم مسح قائمة المحظورين",'parse_mode'=>"MARKDOWN",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['ban'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "bannambar"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
- ارسل ايدي الشخص لكي اقوم بحظره من البوت
",'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['okban'] = "ok_id";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit();
}
if(preg_match('/([0-9])/i',$text) and $carlos['okban'] == "ok_id"){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$text"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم حظر المستخدم بنجاح
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
]);
$carlos['ban'][] = "$text";
$carlos['okban'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "unbannambar"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
- ارسل ايدي الشخص لكي اقوم بالغاء حظره من البوت
",'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['okunban'] = "ok_id";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit();
}
if(preg_match('/([0-9])/i',$text) and $carlos['okunban'] == "ok_id"){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$text"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم الغاء حظر المستخدم بنجاح
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
]);
$key = array_search($text,$carlos["ban"]);
unset($carlos["ban"][$key]);
$carlos["ban"] = array_values($carlos["ban"]); 
$carlos = json_encode($carlos,true);
$carlos['okunban'] = "done";
file_put_contents("data/carlos.json",$carlos);
}

if($data == "Open"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• اهلا عزيزي في بياناتك الشخصيه في البوت 🤖

-  اليك الازرار التاليه تحت ⤵️
",'parse_mode'=>"Markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'جلب نسخه الاعضاء 👥' ,'callback_data'=>"OpenCopy"]],
[['text'=>'جلب نسخه الاعدادات ⚙' ,'callback_data'=>"Openstengs"]],
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "OpenCopy"){
bot('senddocument', [
'chat_id' =>$admin,
'document' =>new CURLFile("data/members.json"),
'caption'=>"• اليك النسخة الاعضاء ✅
عدد الاعضاء ( $md3 ).
",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($data == "Openstengs"){
bot('senddocument', [
'chat_id' =>$admin,
'document' =>new CURLFile("data/carlos.json"),
'caption'=>"• اليك النسخة الاعدادات ⚙
",
'reply_to_message_id'=>$message->message_id, 
]);
}
if($data == "addfiles"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"حسنأ عزيزي ارسل لي الملف المطلوب 📤
⎯ ⎯ ⎯ ⎯",'parse_mode'=>"Markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['addfiles'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
$name_id = $message->document->file_name;
if($message->document and $carlos['addfiles'] == "no"){
if($name_id == "members.json" or $name_id == "carlos.json"){
$file = "https://api.telegram.org/file/bot".API_KEY."/".bot('getfile',['file_id'=>$message->document->file_id])->result->file_path;
file_put_contents("data/$name_id",file_get_contents($file));
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"تم رفعة نسخة الاعضاء بنجاح 📤
الملف ( `$name_id` ).
",'parse_mode'=>"Markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['addfiles'] = "off";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if($data == "1"){
for($i=0;$i<count($groups);$i++){
$nambrgropu = bot('getchatmemberscount',['chat_id'=>$groups[$i]])->result;
$tgnames = "$nambrgropu";
}
$t = "$tgnames\n";
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand"],
'parse_mode'=>"Markdown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'مسح الاحصائيه 🗑  .' ,'callback_data'=>"lstadel"]],
[['text'=>'• رجوع • ' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "lstadel"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
حسنأ عزيزي انته متأكد من حذف الاحصائيات 
عذرأ اولأ عليك ضغط علي نسخ الاحصائيات 
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'نسخ الاحصائيات .' ,'callback_data'=>"Copyahs"]],
[['text'=>'استعادة الاحصائيات .' ,'callback_data'=>"asahs"]],
[['text'=>'نعم ' ,'callback_data'=>"dellahs"],['text'=>'لا ' ,'callback_data'=>"1"]],
[['text'=>'• رجوع • ' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "dellahs"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم تنظيف جميع الاحصائيات 🗑.
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lstadel"]],
]])
]);
$meca['members'] = okdell;
file_put_contents("data/members.json",json_encode($meca));
}
if($data == "Copyahs"){
$cc = file_get_contents('data/members.json');
file_put_contents("data/Copy.json",$cc);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم نسخ جميع الاحصائيات 
يمكنك ب اي وقت استعادة الاحصائيات 
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lstadel"]],
]])
]);
}
if($data == "asahs"){
$cc = file_get_contents('data/Copy.json');
file_put_contents("data/members.json",$cc);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم استعادة جميع الاحصائيات ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع ↩' ,'callback_data'=>"lstadel"]],
]])
]);
}

if($data == "4"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• مرحبا بك في قسم رساله الترحيب (/start) 🌾
- ستظهر هذه الرساله عند ارسال (/start) الى البوت الخاص بك 
- رساله الترحيب : $start

",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'الاختصارات  ' ,'callback_data'=>"ت"]],
[['text'=>'الازرار الشفافة  ' ,'callback_data'=>"Zhang"]],
[['text'=>'مسح رساله ' ,'callback_data'=>"unset start"],['text'=>'تعين الرساله ' ,'callback_data'=>"setstart"]],
[['text'=>'رد على الرسائل : ✅ ' ,'callback_data'=>"8ل"]],
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "startsho" and $chat_id == $admin){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>" رساله start 👇  $start",'parse_mode'=>"Markdown",
'reply_to_meesage_id'=>$message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
}
if($data == "unset start"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• تم مسح رساله start والرجوع الى الرساله الاصلية !
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['start'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "setstart"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
 • ارسال الان الكليشه .

",'parse_mode'=>"Markdown",
'reply_to_meesage_id'=>$message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['ok'] = "ok_start";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['ok'] == "ok_start"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم الحفظ بنجاح
$text
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['ok'] = "no";
$carlos['start'] = $text;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
$addbanlst = count($carlos['ban']);
if($data == "lastban"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
مرحبا بك في قسم الاحصائيات 📊

• عدد المسخدمين الكلي : $countall
- عدد الخاص بك : $countall
- عدد الكروبات والقنوات : $md5

• عدد المحظورين : $addbanlst

• عدد المتفاعلين اليوم : $em1
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'المحظورين ( '.$addbanlst.' )' ,'callback_data'=>"##"]],
[['text'=>'حظر' ,'callback_data'=>"bannambar"],['text'=>'الغاء حظر' ,'callback_data'=>"unbannambar"]],
[['text'=>'عرض المحظورين' ,'callback_data'=>"lstesban"],['text'=>'مسح المحظورين' ,'callback_data'=>"dellastban"]],
[['text'=>'قسم الاذاعه ' ,'callback_data'=>"10"]],
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['okunban'] = "done";
$carlos['okban'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "lstesban" and $carlos['ban'] != null){
$banlast = $carlos['ban'];
for($z = 0;$z <= count($banlast)-1;$z++){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$banlast[$z]"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
$result = $result."- [$banname](https://t.me/$banuser) - $banid"."\n";
}
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
اليك قائمة المحظورين : $result
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
exit();
}
if($data == "lstesban" and $carlos['ban'] == null){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"لايوجد محظور حاليأ",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
}
if($data == "dellastban"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"تم مسح قائمة المحظورين",'parse_mode'=>"MARKDOWN",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['ban'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "bannambar"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*- ارسل ايدي الشخص او معرف الشخص لكي اقوم بحظره من البوت*",'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['okban'] = "ok_id";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit();
}
if(preg_match('/([0-9])/i',$text) and $carlos['okban'] == "ok_id"){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$text"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
- تم حظر العضو بنجاح ✅
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
]);
$carlos['ban'][] = "$text";
$carlos['okban'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "unbannambar"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*- ارسل ايدي الشخص او معرف الشخص لكي اقوم بالغاء حظره من البوت*",'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"lastban"]],
]])
]);
$carlos['okunban'] = "ok_id";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit();
}
if(preg_match('/([0-9])/i',$text) and $carlos['okunban'] == "ok_id"){
$apiban = json_decode(file_get_contents("http://api.telegram.org/bot$API_KEY/getChat?chat_id=$text"));
$banuser =$apiban->result->username;
$banname =$apiban->result->first_name;
$banid =$apiban->result->id;
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
- تم الغاء حظره بنجاح ✅
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
]);
$key = array_search($text,$carlos["ban"]);
unset($carlos["ban"][$key]);
$carlos["ban"] = array_values($carlos["ban"]); 
$carlos = json_encode($carlos,true);
$carlos['okunban'] = "done";
file_put_contents("data/carlos.json",$carlos);
}

if($data == "dellahs"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم تنظيف جميع الاحصائيات 🗑.
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع ↩' ,'callback_data'=>"lstadel"]],
]])
]);
$meca['members'] = okdell;
file_put_contents("data/members.json",json_encode($meca));
}
if($data == "Copyahs"){
$cc = file_get_contents('data/members.json');
file_put_contents("data/Copy.json",$cc);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم نسخ جميع الاحصائيات 
يمكنك ب اي وقت استعادة الاحصائيات 
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع • ' ,'callback_data'=>"lstadel"]],
]])
]);
}
if($data == "asahs"){
$cc = file_get_contents('data/Copy.json');
file_put_contents("data/members.json",$cc);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
تم استعادة جميع الاحصائيات ✅
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"lstadel"]],
]])
]);
}
if($data == "5"){
if ($from_id == $admin) {
$key=[];
foreach ($carlos['admin'] as $ad){
$key[inline_keyboard][]=[[text=>"$ad",callback_data=>"del#$ad"]];
}
$key[inline_keyboard][]=[[text=>"• اضافه ادمن جديد • ",callback_data=>"add_admin"]];
$key[inline_keyboard][]=[[text=>"رجوع",callback_data=>"back"]];
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• مرحبا بك في الادمنيه 👮‍♀️
- يمكنك رفع 5 ادمنيه في البوت او حذفهم 

- يمكن للادمنيه تحكم في لوحه البوت مثلك ولا يمكنهم رفع ادمنيه او استلام رسائل الموجهة او سايت او تواصل .
",
reply_markup=>json_encode($key)
]);
}
}
$ex = explode("#", $data);
if($ex[0] == "del"){
$ser = array_search($ex[1],$carlos["admin"]);
unset($carlos["admin"][$ser]);
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
$key=[];
foreach ($carlos['admin'] as $ad){
$key[inline_keyboard][]=[[text=>"$ad",callback_data=>"del#$ad"]];
}
$key[inline_keyboard][]=[[text=>"• اضافه ادمن جديد •",callback_data=>"add_admin"]];
$key[inline_keyboard][]=[[text=>"• رجوع •",callback_data=>"back"]];
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
reply_markup=>json_encode($key)
]);
}
if($data == "add_admin"){
if ($from_id == $admin) {
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• ارسل ايدي الشخص الان  !
",
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ok'] = "ok_admin";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if($text and $carlos['ok'] == "ok_admin" and !in_array($text,$members)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
$text ليس عضو بالبوت ⚠️
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
}
$test = $carlos['admin'];
if($text and $carlos['ok'] == "ok_admin" and in_array($text,$test)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• هو بالفعل ادمن !
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['ok'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit();
}
if($text and $carlos['ok'] == "ok_admin" and in_array($text,$members)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم الاضافه الى$text  الادمنيه بنجاح
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['admin'][] = $text;
$carlos['ok'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['ok'] == "ok_admin" and in_array($text,$members)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم الاضافه الى$text  الادمنيه بنجاح
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"back"]],
]])
]);
$carlos['admin'][] = $text;
$carlos['ok'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "10"){
for($i=0;$i<count($groups);$i++){
$nambrgropu = bot('getchatmemberscount',['chat_id'=>$groups[$i]])->result;
$tgnames = "$nambrgropu";
}
$t = "$tgnames + ";
bot('EditMessageText',[
'chat_id'=>$chat_id, 
'message_id'=>$message_id,
'text'=>$XQ_3X["sand"],
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'اذاعة للكل' ,'callback_data'=>"send_text"],['text'=>'اذاعة توجيه للكل' ,'callback_data'=>"send_rep"]],
[['text'=>'اذاعة للخاص' ,'callback_data'=>"send_text1"],['text'=>'اذاعة توجيه للخاص' ,'callback_data'=>"send_rep1"]],
[['text'=>'اذاعة كروبات' ,'callback_data'=>"send_text2"],['text'=>'اذاعة توجيه كروبات' ,'callback_data'=>"send_rep2"]],
[['text'=>'رجوع' ,'callback_data'=>"back"]],
]])
]);
$carlos['data'] = "no";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "send_text"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand5"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'رجوع' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_text";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_text" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand6"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($groups);$i++){
bot('sendMessage',[
'chat_id'=>$groups[$i],
'text'=>$text,
'parse_mode'=>"html",
'parse_mode'=>"Markdown",
]);
}
for($i=0;$i<count($members);$i++){
bot('sendMessage',[
'chat_id'=>$members[$i],
'text'=>$text,
'parse_mode'=>"html",
'parse_mode'=>"Markdown",
]);
}
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "send_rep"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand7"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_rep";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_rep" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand8"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($groups);$i++){
bot('forwardMessage',[
'chat_id'=>$groups[$i],
'from_chat_id'=>$from_id,
'message_id'=>$message->message_id
]);
}
for($i=0;$i<count($members);$i++){
bot('forwardMessage',[
'chat_id'=>$members[$i],
'from_chat_id'=>$from_id,
'message_id'=>$message->message_id
]);
}
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "send_text1"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand1"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_text1";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_text1" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand2"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($members);$i++){
bot('sendMessage',[
'chat_id'=>$members[$i],
'text'=>$text,
'parse_mode'=>"html",
'parse_mode'=>"Markdown",
]);
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
}
if($data == "send_rep1"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand9"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_rep1";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_rep1" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand10"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($members);$i++){
bot('forwardMessage',[
'chat_id'=>$members[$i],
'from_chat_id'=>$from_id,
'message_id'=>$message->message_id
]);
}
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "send_text2"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand3"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_text2";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_text2" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand4"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($groups);$i++){
bot('sendMessage',[
'chat_id'=>$groups[$i],
'text'=>$text,
'parse_mode'=>"html",
'parse_mode'=>"Markdown",
]);
}
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($data == "send_rep2"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$XQ_3X["sand11"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
$carlos['data'] = "ok_rep2";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
if($text and $carlos['data']== "ok_rep2" and $text != "/start" and $from_id == $admin){
bot("sendmessage",[
"chat_id"=>$chat_id,
"text"=>$XQ_3X["sand12"],'parse_mode'=>"Markdown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>'• رجوع •' ,'callback_data'=>"10"]],
]])
]);
for($i=0;$i<count($groups);$i++){
bot('forwardMessage',[
'chat_id'=>$groups[$i],
'from_chat_id'=>$from_id,
'message_id'=>$message->message_id
]);
}
$carlos['data'] = "done";
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
}
#------------(carlos)------------#
if($data == "redd"){
      foreach($carlos['carlos'] as $f5f7 => $carloss){
$reply_markup[] = [['text'=>$carloss['name'],'callback_data'=>"null"],['text'=>"🗑",'callback_data'=>'add_red|'.$f5f7]];
}
foreach($carlos['links'] as $f5f7 => $carloss){
$reply_markup[] = [['text'=>$carloss['name'],'url'=>$f5f7]];
}
$reply_markup[] = [['text'=>"اضافه رد جديد",'callback_data'=>"add_red"],['text'=>"الردود : مفعل ",'callback_data'=>"u41"]];
$reply_markup[] =[['text'=>"رجوع",'callback_data'=>"back"]];
$reply_markup = json_encode(['inline_keyboard'=>$reply_markup,]);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*• مرحبا بك في قسم الردود 👮‍♀️*

- يمكنك اضافه ردود وحذفها 
- يمكنك استخدام الاوامر (اضف رد-مسح رد) 

*- اضغط على نص الزر لعرض محتواه .*
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"markdown",
 'reply_markup'=>$reply_markup,
]);
file_put_contents("set.txt",".");
$carlos['n'] = null;
$carlos['mode'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
  }
///////حذف الزر////
$zdelete = explode("|",$data);
if($data == "add_red|$zdelete[1]"){    
$name = $carlos['carlos'][$zdelete[1]]['name'];
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>
"
🗑 تم مسح الرد بنجاح.!
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"redd"]],
]
])
]);
unset($carlos['carlos'][$zdelete[1]]);
file_put_contents("data/carlos.json",json_encode($carlos,128|34|256));
}




if($data == "add_red"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• ارسل الكلمة الان .
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"redd"]],
]
])
]);
$carlos['mode'] = 'add';
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit;
}
if($text != '/start' and $text != null and $carlos['mode'] == 'add'){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"
*• ارسل الرد الان , يمكنك ارسال ( نص او ميديا )*

- يمكنك وضع بعض الاضافات الى الرد من خلال استخدام الاهاشتاكات التاليه :

1. `#id` : لوضع ايدي الشخص 
2. `#username` : لوضع اسم مستخدم الشخص مع اضافه @ 
3. `#name` : لوضع اسم الشخص
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"redd"]],
]
])
]);
$carlos['n'] = $text;
$carlos['mode'] = 'addm';
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
exit;
}
if($text != '/start' and $carlos['mode'] == 'addm'){
$code = $carlos['n'];
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"
- تم حفط الرد بنجاح
",
'parse_mode'=>"MarkDown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• اضافة رد جديد •",'callback_data'=>"add_red"]],
[['text'=>"• رجوع •",'callback_data'=>"redd"]],
]
])
]);
$carlos['carlos'][$code]['name'] = $carlos['n'];
$carlos['carlos'][$code]['mo'] = $text;
$carlos['n'] = null;
$carlos['mode'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,32|128|265));
file_put_contents("sends.txt","");
}
if($carlos['carlos'][$text]!=null){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>$carlos['carlos'][$text]['mo'],
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
]);
}






if($data == "zrar"){
      foreach($carlos['carloss'] as $f5f7 => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'callback_data'=>'nm|'.$f5f7],['text'=>" 🗑 ",'callback_data'=>'vu|'.$f5f7]];
}
foreach($carlos['links'] as $f5f7 => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'url'=>$f5f7]];
}
$reply_markup[] = [['text'=>"تعديل زر جديد",'callback_data'=>"addbtn"]];
$reply_markup[] = [['text'=>" قسم الازرار الشفافه ",'callback_data'=>"Zhang"]];
$reply_markup[] =[['text'=>"رجوع",'callback_data'=>"back"]];
$reply_markup = json_encode(['inline_keyboard'=>$reply_markup,]);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*• مرحبا بك في قسم تعديل ازرار البوت 🤖*

- يمكنك اضافه تعديلات للازرار وحذفها 
*- اضغط على نص الزر لعرض التعديل الذي اصبح عليه الزر .*
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"markdown",
 'reply_markup'=>$reply_markup,
]);
file_put_contents("set.txt",".");
$carlos['n'] = null;
$carlos['mode'] = null;
save($carlos);
  }
$zhend = explode("|",$data);
if($data == "zh|$zhend[1]"){
$pri = $carlos['carloss'][$zhend[1]]['mo'];
$name = $carlos['carloss'][$zhend[1]]['name'];
$Type = $carlos['carloss'][$zhend[1]]['Type'];
if($Type == "EditMessageText"){
$offer = "تعديل الرساله";
}
if($Type == "sendMessage"){
$offer = "رساله جديده";
}
$fro = "محتوى نصي";
bot('editMessageText',[
      'chat_id'=>$chat_id,
      'message_id'=>$message_id,
      'text'=>"*• اسم الزر : $name*

- مسار الزر : home

- نوع الزر : *$fro*

$pri",
      'reply_to_message_id'=>$message->message_id,
      'parse_mode'=>"MarkDown",
      'disable_web_page_preview'=> true ,
     'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"مسح الزر",'callback_data'=>'delete|'.$zhend[1]]],
[['text'=>"طريقة عرض النص : ".$offer,'callback_data'=>'offer|'.$zhend[1]]],
[['text'=>"رجوع",'callback_data'=>"zrar"]],
]
])
      ]);}      
if($data == "Zhang"){
            foreach($carlos['carloss'] as $f5f7 => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'callback_data'=>'zh|'.$f5f7]];
}
foreach($carlos['links'] as $f5f7 => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'url'=>$f5f7]];
}
$reply_markup[] =[['text'=>" +",'callback_data'=>"addbtn"]];
$reply_markup[] =[['text'=>" قسم تعديل الازار",'callback_data'=>"zrar"],['text'=>"الازرار الاساسية : ✅",'callback_data'=>"cc"]];
$reply_markup[] =[['text'=>" قسم نسخ الازرار",'callback_data'=>"cc"]];
$reply_markup[] =[['text'=>"رجوع",'callback_data'=>"back"]];
$reply_markup = json_encode(['inline_keyboard'=>$reply_markup,]);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
*• مرحبا بك في قسم الازرار الشفافة ✨*

- يمكنك اضافه ازرار شفافة او حذفها ( لا يمكنك حذف الازرار الاساسية ولاكن يمكنك تعديلها من قسم تعديل الازرار )
",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"markdown",
 'reply_markup'=>$reply_markup,
]);
file_put_contents("set.txt",".");
$carlos['n'] = null;
$carlos['mode'] = null;
save($carlos);
  }
$zhend = explode("|",$data);
if($data == "nm|$zhend[1]"){
$pri = $carlos['carloss'][$zhend[1]]['mo'];
$name = $carlos['carloss'][$zhend[1]]['name'];
$Type = $carlos['carloss'][$zhend[1]]['Type'];
if($Type == "EditMessageText"){
$offer = "تعديل الرساله";
}
if($Type == "sendMessage"){
$offer = "رساله جديده";
}
$fro = "محتوى نصي";
bot('sendMessage',[
      'chat_id'=>$chat_id,
      'message_id'=>$message_id,
      'text'=>" 
- الزر : $name

- التعديل : $pri      
",
'parse_mode'=>"MarkDown",
'reply_to_message_id'=>$message->message_id,
]);
}
$zhend = explode("|",$data);
if($data == "vu|$zhend[1]"){
$pri = $carlos['carloss'][$zhend[1]]['mo'];
$name = $carlos['carloss'][$zhend[1]]['name'];
$Type = $carlos['carloss'][$zhend[1]]['Type'];
if($Type == "EditMessageText"){
$offer = "تعديل الرساله";
}
if($Type == "sendMessage"){
$offer = "رساله جديده";
}
$fro = "محتوى نصي";
bot('editMessageText',[
      'chat_id'=>$chat_id,
      'message_id'=>$message_id,
      'text'=>"
اوه عزيزي هل متاكد من حذف الزر 🫥 
",
      'reply_to_message_id'=>$message->message_id,
      'parse_mode'=>"MarkDown",
      'disable_web_page_preview'=> true ,
     'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"نعم",'callback_data'=>'delete|'.$zhend[1]]],
[['text'=>"رجوع",'callback_data'=>"zrar"]],
]
])
      ]);}      
      
$zoffer = explode("|",$data);
if($data == "offer|$zoffer[1]"){
if($carlos['carloss'][$zoffer[1]]['Type']!="EditMessageText"){
bot('answerCallbackQuery',[
   'callback_query_id'=>$update->callback_query->id,
        'text'=>'تعديل الرساله',
        
      ]);
  
$iu = "EditMessageText";
}else{
bot('answerCallbackQuery',[
   'callback_query_id'=>$update->callback_query->id,
        'text'=>'رساله جديده',
        
      ]);
  
$iu ="sendMessage";
}
$Type = $carlos['carloss'][$zoffer[1]]['Type'];
if($Type == "EditMessageText"){
$offer = "رساله جديده";
}
if($Type == "sendMessage"){
$offer = "تعديل الرساله";
}
$carlos['carloss'][$zoffer[1]]['Type'] = $iu;
file_put_contents('data/carlos.json', json_encode($carlos,128|34|256));
bot('editMessageReplyMarkup',[
'chat_id'=>$update->callback_query->message->chat->id,
'message_id'=>$update->callback_query->message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"مسح الزر",'callback_data'=>'delete|'.$zhend[1]]],
[['text'=>"طريقة عرض النص : ".$offer,'callback_data'=>'offer|'.$zhend[1]]],
[['text'=>"رجوع",'callback_data'=>"zrar"]],
]])
]);    
}

///////حذف الزر////
$zdelete = explode("|",$data);
if($data == "delete|$zdelete[1]"){    
$name = $carlos['carloss'][$zdelete[1]]['name'];
bot('answerCallbackQuery',['callback_query_id'=>$update->callback_query->id,
        'text'=>'تم المسح بنجاح ✅ ',
      ]);
      sleep (1);
for($i = 0;$i <= count($sttingsid)-1;$i++){
$fromid = $sttingsid[$i]; 
$membr=json_decode(file_get_contents("data/$fromid.json"),true);
if($membr[$fromid]["l"] > 0){
$move["bob"][$fromid] =$membr[$fromid]["l"];
file_put_contents("data/$from_id.json",json_encode($move,128|34|256)); 
}
}
$array = [];

foreach($move["bob"] as $key => $value){
$array[$key] = $value;
}
$txt = null;
for($i=1;$i<=5;$i++){
if(!empty($array)){
$arrayValues = array_values($array);
$maxKey = array_search(max($arrayValues),$arrayValues);
$member = array_keys($array)[$maxKey];
$count = $arrayValues[$maxKey];
$kk = array("1","2","3","4","5");
$kk1 = array("🥇","🥈","🥉","🏅","🏅");
$ii = str_replace($kk, $kk1, $i);
$k = $membr[$member]['s']; 
$txt .= "$ii :($count) -> [$member](tg://user?id=$member)\n";
unset($array[$member]);
}
}
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
• تم المسح اضغط رجوع  للرجوع للقائمه الرئيسية .
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"zrar"]],
]
])
]);
unset($carlos['links'][$zdelete[1]]);
unset($carlos['carloss'][$zdelete[1]]);
file_put_contents("data/carlos.json",json_encode($carlos,128|34|256));
}


if($data == "addbtn"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"*• ارسل الان اسم الزر المراد تعديله*
- عليك كتابه اسم الزر بشكل صحيح ...!
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"zrar"]],
]
])
]);
$carlos['mode'] = 'ssdr';
file_put_contents("data/carlos.json",json_encode($carlos,128|34|256));
exit;
}
if($text != '/start' and $text != null and $carlos['mode'] == 'ssdr'){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" 
",
'parse_mode'=>"MarkDown",
'reply_to_message_id'=>$message->message_id,
]);
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>" • ارسل الان النص الذي تريد كتابته بدل ' $text ' 
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"zrar"]],
]
])
]);
$carlos['n'] = $text;
$carlos['mode'] = 'czhsu';
file_put_contents("data/carlos.json",json_encode($carlos,128|34|256));
exit;
}
if($text != '/start' and $carlos['mode'] == 'czhsu'){
$code = $carlos['n'];
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"
• تم الحفظ .
",
'parse_mode'=>"MarkDown",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([ 
'inline_keyboard'=>[
[['text'=>"• رجوع •",'callback_data'=>"zrar"]],
]
])
]);
$carlos['carloss'][$code]['name'] = $carlos['n'];
$carlos['carloss'][$code]['mo'] = $text;
$carlos['carloss'][$code]['Type'] = "EditMessageText";
$carlos['n'] = null;
$carlos['mode'] = null;
file_put_contents("data/carlos.json",json_encode($carlos,128|34|256));
file_put_contents("sends.txt","");
}
$start = "
$start
";
if($text == "/start"){
foreach($carlos['carloss'] as $ced => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'callback_data'=>$ced]];
}
foreach($carlos['links'] as $ced => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'url'=>$ced]];
}
$reply_markup = json_encode(['inline_keyboard'=>$reply_markup,]);
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"$start",
'reply_to_message_id'=>$message->message_id,
'parse_mode'=>"MarkDown",
 'reply_markup'=>$reply_markup,
]);
}


if($data == "yycsh"){
foreach($carlos['carloss'] as $ced => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'callback_data'=>$ced]];
}
foreach($carlos['links'] as $ced => $carlosss){
$reply_markup[] = [['text'=>$carlosss['name'],'url'=>$ced]];
}
$reply_markup = json_encode(['inline_keyboard'=>$reply_markup,]);
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>$start,
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
 'reply_markup'=>$reply_markup,
]);}

$price = $carlos['carloss'][$data]['mo'];
$price = str_replace('#name', "[$name](tg://user?id=$from_id)",$price);
$price = str_replace('#username', "[$use]",$price);
$price = str_replace('#id', "$from_id",$price);
$name = $carlos['carloss'][$data]['name'];
$Type = $carlos['carloss'][$data]['Type'];
if($Type == "EditMessageText"){
$reply_p[] = [['text'=>"رجوع",'callback_data'=>"yycsh"]];
$reply_p = json_encode(['inline_keyboard'=>$reply_p,]);
}
if($price != null){
bot($Type,[
      'chat_id'=>$chat_id,
      'message_id'=>$message_id,
      'text'=>$price,
      'reply_to_message_id'=>$message->message_id,
      'parse_mode'=>"MarkDown",
 'reply_markup'=>$reply_p,
      ]);
  }
  
  
  
if($data == "bbuuii"){
bot('EditMessageText',[
'chat_id'=>$chat_id,
'message_id'=>$message_id,
'text'=>"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:$gift50","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:$gift1", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]])
]);
}
  
  
  
  
  
$infobot = json_decode(file_get_contents("https://api.telegram.org/bot$token/getme"), 1);
$userbot = $infobot["result"]["username"];
$idBot = $infobot["result"]["id"];
date_default_timezone_set("Asia/Baghdad");
$time = date("h:i a");
$year = date("Y");
$month = date("n");
$day = date("j");
$h = date("h");
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$message_id = $message->message_id;
$chat_id = $message->chat->id;
$from_id = $message->from->id;
$first_name = $message->from->first_name;
$username = $message->from->username;
$text = $message->text;
$fromid = $update->callback_query->from->id;
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
$admin = array("5180881216","$admin");
$setting = json_decode(file_get_contents("setting.json"), 1);
$mode = $setting["1$from_id"];
$gift = $setting["gift"];
$gift1 = $setting["gift1"];
$invite = $setting["setjoincoin"];
$settm = $setting["settm"];
$coa = $setting["coa"];
$gift50 = $setting["gift50"];
$gift5 = $setting["gift5"];
$chtm = $setting["setchs"];
$priceforward = $setting["priceforward"];
$setgiftcoin = $setting["setgiftcoin"];
$pricez = $setting["pricez"];
$dev = $setting["dev"];
$name = $message->from->first_name;
$type       = $message->chat->type;

$private = $type == "private";
$supergroup = $type == "supergroup";
if (true) {
if ($text) {
$coins = $setting[$from_id]["coins"];
} else {
$coins = $setting[$chat_id2]["coins"];
}
}

$KEYBACK1 = json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h1"]]
]
]);
$KEYBACK2 = json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
]);
if ($gift1 != "✅") {
    $KEY = json_encode([
            "inline_keyboard" => [
            [["text" => "عدد نقاطك$coins", "callback_data" => "coins"]],
              [["text" => "إنقر هنا لرفع مشتركين 👤✅", "callback_data" => "visco"]],
        [["text" => "تجميع النقاط ➕💠", "callback_data" => "getcoin"],
            ["text" => "تحويل نقاط ♻️", "callback_data" => "forwardcoin"]],       
            [["text" => "مشاهدة تمويلاتي 👤👁‍🗨", "callback_data" => "tmc"],["text" => "معلومات حسابك 🪪", "callback_data" => "infoaccount"]],
             [["text" => "الهدية اليومية 🎁", "callback_data" => "gift"]],
             [["text" => "شحن نقاط لحسابك تلقائيا 💎💱", "url" => "t.me/O_1_W"]],
                      [["text" => "رابط الدعوة ♾", "callback_data" => "yourlink"],["text" => "التعليمات البوت 🛠", "url" => "t.me/aviscvio"]],            
              [["text" => "القوانين ⛔️", "url" => "t.me/gviisco"], ["text" => "شراء نقاط 👨🏻‍💻💰", "url" => "t.me/mlunerks/3"]],          
        ]
    ]);
} elseif ($gift1 == "✅") {
    $KEY = json_encode([
         "inline_keyboard" => [
            [["text" => "عدد نقاطك$coins", "callback_data" => "coins"]],
              [["text" => "إنقر هنا لرفع مشتركين 👤✅", "callback_data" => "visco"]],
        [["text" => "تجميع النقاط ➕💠", "callback_data" => "getcoin"],
            ["text" => "تحويل نقاط ♻️", "callback_data" => "forwardcoin"]],       
            [["text" => "مشاهدة تمويلاتي 👤👁‍🗨", "callback_data" => "tmc"],["text" => "معلومات حسابك 🪪", "callback_data" => "infoaccount"]],
             [["text" => "الهدية اليومية 🎁", "callback_data" => "gift"]],
              [["text" => "شحن نقاط لحسابك تلقائيا 💎💱", "url" => "t.me/O_1_W"]],
                      [["text" => "رابط الدعوة ♾", "callback_data" => "yourlink"],["text" => "التعليمات البوت 🛠", "url" => "t.me/aviscvio"]],            
              [["text" => "القوانين ⛔️", "url" => "t.me/gviisco"], ["text" => "شراء نقاط 👨🏻‍💻💰", "url" => "t.me/mlunerks/3"]],        
        ]
    ]);
}
$type = $message->chat->type;
if ($time == "12:00 am") {
unlink("gift.txt");
}
if (strpos($text, "/start ") !== false and $private) {
if (!in_array($from_id, $setting["user"])) {
$sr = str_replace("/start ", "", $text);
$coins = $invite + $coins;
bot("SendMessage", [
"chat_id" => $sr,
"text" => "• قام : [$name](tg://openmessage?user_id=$from_id) بالدخول الى الرابط الخاص وحصلت على $invite نقطه ✨
• عدد عدد نقاطك$coins",
"parse_mode" => "markdown"
]);
$setting[$sr]["inv"] += 1;
$setting[$sr]["coins"] += $invite;
file_put_contents("setting.json", json_encode($setting));
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "• قمت بالدخول الى الرابط الدعوه الخاص بصديقك وحصل على $invite نقطه ✨"
]);
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>
━━━━━━━━━━━━━━━━━━━━━━━━
                     『 بوت تمويل  』           
━━━━━━━━━━━━━━━━━━━━━━━━
اهلا بك عزيزي في بوت تمويل 🎉 القنوات والمجموعات بواسطة تجميع نقاط فقط 🍿
━━━━━━━━━━━━━━━━━━━━━━━━
يمكنك اختيار الأزرار بالأسفل  🛍️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</b>

$txtfree",
"parse_mode" => "html",
'disable_web_page_preview' => true,
"reply_markup" => $KEY
]);
} else {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>
━━━━━━━━━━━━━━━━━━━━━━━━
                     『 بوت تمويل  』           
━━━━━━━━━━━━━━━━━━━━━━━━
اهلا بك عزيزي في بوت تمويل 🎉 القنوات والمجموعات بواسطة تجميع نقاط فقط 🍿
━━━━━━━━━━━━━━━━━━━━━━━━
يمكنك اختيار الأزرار بالأسفل  🛍️
━━━━━━━━━━━━━━━━━━━━━━━━
</b>

",
"parse_mode" => "html",
'disable_web_page_preview' => true,
"reply_markup" => $KEY
]);
}
}

 
if ($text == "/start" and $private) {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>
━━━━━━━━━━━━━━━━━━━━━━━━
                     『 بوت تمويل  』           
━━━━━━━━━━━━━━━━━━━━━━━━
اهلا بك عزيزي في بوت تمويل 🎉 القنوات والمجموعات بواسطة تجميع نقاط فقط 🍿
━━━━━━━━━━━━━━━━━━━━━━━━
يمكنك اختيار الأزرار بالأسفل  🛍️
━━━━━━━━━━━━━━━━━━━━━━━━
</b>

",
"parse_mode" => "html",
'disable_web_page_preview' => true,
"reply_markup" => $KEY
]);
}
if($message and !in_array($from_id, $setting["user"]) and $gift50 == "✅" and $private and !in_array($from_id,$admin)) {
$setting["user"][] = $from_id;
$setting["$from_id"]["coins"]+=$gift5;
file_put_contents("setting.json", json_encode($setting));
bot("SendMessage",[
"chat_id"=>$chat_id,
"text"=>"حصلت على $gift5 نقطه هدية من المطور ",
]);
}
if ($data == "h2") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>
━━━━━━━━━━━━━━━━━━━━━━━━
                     『 بوت تمويل  』           
━━━━━━━━━━━━━━━━━━━━━━━━
اهلا بك عزيزي في بوت تمويل 🎉 القنوات والمجموعات بواسطة تجميع نقاط فقط 🍿
━━━━━━━━━━━━━━━━━━━━━━━━
يمكنك اختيار الأزرار بالأسفل  🛍️
━━━━━━━━━━━━━━━━━━━━━━━━
</b>

",
"parse_mode" => "html",
'disable_web_page_preview' => true,
"reply_markup" => $KEY
]);
}
if ($data == "forwardcoin") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>• بمكنك تحويل عدد من النقاط الى شخص اخر من هنا🌐

- فقط ارسل عدد النقاط التي تريد ارسالها وسيتم صنع رابط ارسله الى الشخاص المراد استلام نقاط

- عموله التحويل : $priceforward</b>

$txtfree",
"parse_mode" => "html",
"reply_markup" => $KEYBACK2
]);
$setting[$chat_id2]["forward"] = "on";
file_put_contents("setting.json", json_encode($setting));
}
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=$idch");
$jsonlink = json_decode($getlink, true);
$getlinkde = $jsonlink['result'];
$d = $pricez * 2;
if ($allchannel[$z] != null and $private) {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "• تم خصم $d من عدد نقاطك ⭕️, بسبب مغادره قناة[$namech]($getlinkde) اعطيتك نقاط مقابل الاشتراك بها !!!!",
"parse_mode" => "markdown"
]);
unset($setting["$from_id"]["chrubo"][$z]);
$setting["$from_id"]["chrubo"] = array_values($setting["$from_id"]["chrubo"]);
file_put_contents("setting.json", json_encode($setting));
$coin = $setting["$from_id"]["coins"];
$pluscoin = $coin - $d;
$setting["$from_id"]["coins"] -= "$d";
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}
$allchannel = $setting[$chat_id2]["chrubo"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=$idch");
$jsonlink = json_decode($getlink, true);
$getlinkde = $jsonlink['result'];
$d = $pricez * 2;
if ($allchannel[$z] != null) {
bot("SendMessage", [
"chat_id" => $chat_id2,
"text" => "• تم خصم $d من عدد نقاطك ⭕️, بسبب مغادره قناة[$namech]($getlinkde) اعطيتك نقاط مقابل الاشتراك بها !!!!",
"parse_mode" => "markdown"
]);
unset($setting["$chat_id2"]["chrubo"][$z]);
$setting["$chat_id2"]["chrubo"] = array_values($setting["$chat_id2"]["chrubo"]);
file_put_contents("setting.json", json_encode($setting));
$coin = $setting["$chat_id2"]["coins"];
$pluscoin = $coin - $d;
$setting["$chat_id2"]["coins"] -= "$d";
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}
$rand = substr(str_shuffle("0123456789abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ"), -18);
if ($text and $setting[$from_id]["forward"] == "on" and preg_match("/([0-9])/i", $text)) {
if ($coins > $priceforward) {
$ca = $text + $priceforward;
$c = $text - $priceforward;
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
• تم خصم $ca من عدد نقاطك

- عموله التحويل : $priceforward

• رابط تحويل النقاط : https://t.me/$userbot?start=T$rand

• ارسل الرابط للشخص المراد تحويل النقاط له 

• الرابط صالح لمده 15د

- يمكنك الضغط على زر تعطيل الرابط بعد اقل من 15د لكي تقوم بسترداد عدد نقاطك او قم بدخول على الرابط لاسترداد عدد نقاطك",
'disable_web_page_preview' => 'true',
'reply_markup' => json_encode([
"inline_keyboard" => [
[["text" => "تعطيل الرابط", "callback_data" => "breacklink"]],
[["text" => "رجوع", "callback_data" => "h2"]],
]
])
]);
$r = count($setting["forwad"]);
$setting[$from_id]["coins"] -= $c;
$setting["forward"][$rand]["coin"] = $ca;
$setting["forward"][$rand]["niggaa"] = $chat_id;
$setting["forward"][$rand]["count"] = $r;
$setting["forwad"][] = $rand;
$setting[$from_id]["forward"] = " ";
file_put_contents("setting.json", json_encode($setting));
}
}
$ex = explode("T", $text);
$d = $setting["forwad"];
if (preg_match("/^\/(start) (T)/s", $text) and $private) {
if (in_array($ex[1], $d)) {
$c = $setting["forward"][$ex[1]]["coin"];
$v = $c + $coins;
$sed = $setting["forward"][$ex[1]]["niggaa"];
$d1 = $setting["forward"][$ex[1]]["count"];
bot('sendmessage', [
'chat_id' => $chat_id,
'text' => "• تم اضافة $c نقاط الى حسابك ✅
 • بواسطه رابط التحويل من قبل : [$sed](tg://openmessage?user_id=$sed)

 • اصبحت عدد نقاطك$v",
'parse_mode' => "Markdown",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$sed]["forw"] += 1;
$setting[$from_id]["coins"] += $c;
$d1 = array_search($ex[1], $setting["forwad"]);
unset($setting["forwad"][$d1]);
file_put_contents("setting.json", json_encode($setting));
}
}
$dapy = explode("\n", file_get_contents("gift.txt"));
if ($data == "gift") {
if (!in_array($chat_id2, $dapy)) {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
<b> • لقد حصلت على $setgiftcoin نقاط هدية يومية 🎁 </b>
",
"parse_mode" => "html",
"reply_markup" => $KEYBACK2
]);
file_put_contents("gift.txt", $chat_id2 . "\n", FILE_APPEND);
$setting[$chat_id2]["coins"] += $setgiftcoin;
$setting[$chat_id2]["gf"] += 1;
file_put_contents("setting.json", json_encode($setting));
} else {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
<b>• لقد حصلت على الهدية مسبقا , انتظر يوم واعد المحاولة !</b>
",
"parse_mode" => "html",
"reply_markup" => $KEYBACK2
]);
}
}
if ($data == "coins") {
bot('answercallbackquery', [
'callback_query_id' => $update->callback_query->id,
'text' => "
عدد نقاطك ($coins)",
'show_alert' => true,
]);
}
if ($data == "order") {
$i = 0;
$chs = $setting[$chat_id2]["order"];
$Ibotton1 = [];
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$chs[$i]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=$chs[$i]");
$jsonlink = json_decode($getlink, true);
$getlinkde = $jsonlink['result'];
$mem = $setting[$chs[$i]]["member1"];
$em = $setting[$chs[$i]]["member"];
foreach ($chs as $row) {
$Ibotton1['inline_keyboard'][] = [["text" => "$namech", "url" => "$getlinkde"], ["text" => "$mem/$em", "callback_data" => "nnn"]];
$i++;
}
$Ibotton1['inline_keyboard'][] = [["text" => "مشاهدة تمويلاتي 👤👁‍🗨", "callback_data" => "tmc"]];
$Ibotton1['inline_keyboard'][] = [['text' => "رجوع", 'callback_data' => 'h2']];
$reply_markup = json_encode($Ibotton1);
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"

• جميع القنوات او مجموعاتك الجاري تمويلها التابعه لك

- اذا اردت زيادة عدد التمويل فقط قم بتمويل قناتك مجددا سيتم اضافه التمويل الجديد على القديم
",
"parse_mode" => "html",
"reply_markup" => $reply_markup
]);
}
if ($data == "tmc") {
if ($coa < $coins) {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
• ارسل عدد الاعضاء المراد تمويلهم او يمكنك الاختيار من الازرار 🌐

- ملاحضة : كل 1 عضو يساوي $settm نقطه 

- عدد عدد نقاطك$coins",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "طلب الكل", "callback_data" => "allc"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id2]["mode"] = "tmc";
file_put_contents("setting.json", json_encode($setting));
} else {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
• عليك تجميع النقاط ➕💠 اكثر من $coa نقطه !",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "تجميع النقاط", "callback_data" => "getcoin"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
}
}
if ($data == "visco") {
if ($coa < $coins) {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
• ارسل عدد الاعضاء المراد تمويلهم او يمكنك الاختيار من الازرار 🌐

- ملاحضة : كل 1 عضو يساوي $settm نقطه 

- عدد عدد نقاطك$coins",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "طلب الكل", "callback_data" => "allc"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id2]["mode"] = "visco";
file_put_contents("setting.json", json_encode($setting));
} else {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
• عليك تجميع النقاط ➕💠 اكثر من 300 نقطة $coa نقطه !",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "تجميع النقاط", "callback_data" => "getcoin"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
}
}
if ($data == "allc") {
$max = $coins / $settm;
$maxmember2 = floor($max);
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
رائع الان 💜 $maxmember2

- اختر ماذا تريد ان تقوم بتمويله ؟",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "قناة خاصة", "callback_data" => "cdpv"], ["text" => "قناة عامة", "callback_data" => "chgl"]],
[["text" => "مجموعة", "callback_data" => "gp"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id2]["mem"] = "$maxmember2";
file_put_contents("setting.json", json_encode($setting));
}
$mode = $setting[$from_id]["mode"];
if ($text and $mode == "tmc" and preg_match("/([0-9])/i", $text)) {
$max = $coins / $settm;
$maxmember2 = floor($max);
if ($maxmember2 >= $text) {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
رائع الان 💜

- اختر ماذا تريد ان تقوم بتمويله ؟",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "قناة خاصة", "callback_data" => "cdpv"], ["text" => "قناة عامة", "callback_data" => "chgl"]],
[["text" => "مجموعة", "callback_data" => "gp"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id]["mem"] = "$text";
file_put_contents("setting.json", json_encode($setting));
} else {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>• ليس لديك هذه القدر من النقاط 🚫!</b>",
"reply_to_message_id" => $message_id,
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "تجميع النقاط", "callback_data" => "getcoin"]],
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
}
}
if ($data == "chgl") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
- عليك اضافتي الى القناة ومن ثم ترقيتي الى مشرف فيها مع عطائي صلاحيه دعوه المستخدمين🐝

- ثم ارسل معرف القناة او رابط القناة العام

~ اقرأ الخطوات جيدا ❤️",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id2]["mode"] = "chgl";
file_put_contents("setting.json", json_encode($setting));
}
if ($data == "cdpv") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
- عليك اضافتي الى القناة ومن ثم ترقيتي الى مشرف فيها مع عطائي صلاحيه دعوه المستخدمين🐝

- ثم ارسل توجيه من القناة رساله نصيه الى هنا

~ اقرأ الخطوات جيدا ❤️",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$chat_id2]["mode"] = "cdpv";
file_put_contents("setting.json", json_encode($setting));
}
if ($data == "gp") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
- عليك اضافتي الى المجموعة ومن ثم ترقيتي الى مشرف فيها مع عطائي صلاحيه دعوه المستخدمين🐝

-ارسل في المجموعة هذه الرساله : <code>تمويل الكروب</code> 

~ اقرأ الخطوات جيدا ❤️",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
}


if ($data == "getcoin") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
مرحبا بك في قسم تجميع النقاط 📥 .

• يمكنك الحصول على نقاط بطريقتين :

1 - عن طريق الاشتراك في القنوات او المجموعات

2 - عن طريق مشاركة رابط الدعوة ♾ الى اصدقائك و سوف تحصل على $coininv نقطه عند دخول اي شخص الى الرابط الخاص بك


~ اذ كانت طريقه التجميع صعبه راسل المطور لشراء النقاط 💰 .

~ المطـور : $dev",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "الاشتراك في القنوات او المجموعات", "callback_data" => "noturbo"]],
[["text" => "الاشتراك في القنوات (تيربو)", "callback_data" => "turbo"]],
[["text" => "رابط الدعوة ♾", "callback_data" => "yourlink"]],
[["text" => "رجوع", "callback_data" => "h2"]],
]
])
]);
}

$allchannel = $setting["chanel"];
for($z0 = 0;$z0 <= count($allchannel);$z0++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[0]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z1 = 1;$z1 <= count($allchannel);$z1++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[1]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z2 = 2;$z2 <= count($allchannel);$z2++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[2]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z3 = 3;$z3 <= count($allchannel);$z3++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[3]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z4 = 4;$z4 <= count($allchannel);$z4++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[4]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z5 = 5;$z5 <= count($allchannel);$z5++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[5]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z6 = 6;$z6 <= count($allchannel);$z6++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[6]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z7 = 7;$z7 <= count($allchannel);$z7++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[7]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z8 = 8;$z8 <= count($allchannel);$z8++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[8]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
for($z9 = 9;$z9 <= count($allchannel);$z9++){
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=".$allchannel[9]."&user_id=".$chat_id2));
$okchannel = $getchannel->result->status;
if($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator'){
break;
}}
$url0 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z0]");
$getchat0 = json_decode($url0, true);
$namech0 = $getchat0["result"]["title"]; 
$userch0 = $getchat0["result"]["username"]; 
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z1]");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"]; 
$userch1 = $getchat1["result"]["username"]; 
$url2 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z2]");
$getchat2 = json_decode($url2, true);
$namech2 = $getchat2["result"]["title"]; 
$userch2 = $getchat2["result"]["username"]; 
$url3 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z3]");
$getchat3 = json_decode($url3, true);
$namech3 = $getchat3["result"]["title"]; 
$userch3 = $getchat3["result"]["username"]; 
$url4 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z4]");
$getchat4 = json_decode($url4, true);
$namech4 = $getchat4["result"]["title"]; 
$userch4 = $getchat4["result"]["username"]; 
$url5 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z5]");
$getchat5 = json_decode($url5, true);
$namech5 = $getchat5["result"]["title"]; 
$userch5 = $getchat5["result"]["username"]; 
$url6 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z6]");
$getchat6 = json_decode($url6, true);
$namech6 = $getchat6["result"]["title"]; 
$userch6 = $getchat6["result"]["username"]; 
$url7 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z7]");
$getchat7 = json_decode($url7, true);
$namech7 = $getchat7["result"]["title"]; 
$userch7 = $getchat7["result"]["username"]; 
$url8 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z8]");
$getchat8 = json_decode($url8, true);
$namech8 = $getchat8["result"]["title"]; 
$userch8 = $getchat8["result"]["username"]; 
$url9 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z9]");
$getchat9 = json_decode($url9, true);
$namech9 = $getchat9["result"]["title"]; 
$userch9 = $getchat9["result"]["username"]; 
$id0 = $getchat0["result"]["id"]; 
$id1 = $getchat1["result"]["id"]; 
$id2 = $getchat2["result"]["id"]; 
$id3 = $getchat3["result"]["id"]; 
$id4 = $getchat4["result"]["id"]; 
$id5 = $getchat5["result"]["id"]; 
$id6 = $getchat6["result"]["id"]; 
$id7 = $getchat7["result"]["id"]; 
$id8 = $getchat8["result"]["id"]; 
$id9 = $getchat9["result"]["id"]; 
if($data == "turbo" ){
if($id0 == null and $id1 == null and $id2 ==null and $id3 ==null and $id4 == null and $id5 == null and $id6 == null and $df7 == null and $id8 == null and $id9 == null){
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "رابط الدعوة ♾", 'callback_data' => 'yourlink']],
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
}else{
unset($setting[$chat_id2]["turbp"]);
$setting[$chat_id2]["turbp"]= array_values($setting[$chat_id2]["turbp"]);
file_put_contents("setting.json", json_encode($setting));
$setting[$chat_id2]["getjoinchi"][]="$id0";
$setting[$chat_id2]["getjoinchi"][]="$id1";
$setting[$chat_id2]["getjoinchi"][]="$id2";
$setting[$chat_id2]["getjoinchi"][]="$id3";
$setting[$chat_id2]["getjoinchi"][]="$id4";
$setting[$chat_id2]["getjoinchi"][]="$id5";
$setting[$chat_id2]["getjoinchi"][]="$id6";
$setting[$chat_id2]["getjoinchi"][]="$id7";
$setting[$chat_id2]["getjoinchi"][]="$id8";
$setting[$chat_id2]["getjoinchi"][]="$id9";
file_put_contents("setting",json_encode($setting));
$link0 = $setting[$id0]["link"];
$link0 = trim($link0,"https://t.me/");
$link1 = $setting[$id1]["link"];
$link1 = trim($link1,"https://t.me/");
$link2 = $setting[$id2]["link"];
$link2 = trim($link2,"https://t.me/");
$link3 = $setting[$id3]["link"];
$link3 = trim($link3,"https://t.me/");
$link4 = $setting[$id4]["link"];
$link4 = trim($link4,"https://t.me/");
$link5 = $setting[$id5]["link"];
$link5 = trim($link5,"https://t.me/");
$link6 = $setting[$id6]["link"];
$link6 = trim($link6,"https://t.me/");
$link7 = $setting[$id7]["link"];
$link7 = trim($link7,"https://t.me/");
$link8 = $setting[$id8]["link"];
$link8 = trim($link8,"https://t.me/");
$link9 = $setting[$id9]["link"];
$link9 = trim($link9,"https://t.me/");
$allchannel = $setting["chanel"];
bot("EditMessageText",[
"chat_id"=>$chat_id2,
"message_id"=>$message_id2,
"text"=>"
<b> 
• اشترك في القنوات 
- ثم اضغط على التالي للتحصل على $pricez مقابل كل قناة🌎 </b>

• عدد نقاطك الحاليه : $coins


",
"parse_mode"=>"HTML",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>"$namech0",'url'=>"t.me/$link0"]],
[['text'=>"$namech1",'url'=>"t.me/$link1"]],
[['text'=>"$namech2",'url'=>"t.me/$link2"]],
[['text'=>"$namech3",'url'=>"t.me/$link3"]],
[['text'=>"$namech4",'url'=>"t.me/$link4"]],
[['text'=>"$namech5",'url'=>"t.me/$link5"]],
[['text'=>"$namech6",'url'=>"t.me/$link6"]],
[['text'=>"$namech7",'url'=>"t.me/$link7"]],
[['text'=>"$namech8",'url'=>"t.me/$link8"]],
[['text'=>"$namech9",'url'=>"t.me/$link9"]],
[['text'=>"تحقق",'callback_data'=>'turech']],
[['text'=>"•رجوع•",'callback_data'=>'getcoin']],
]
])
]);
}}
$ex = explode("##", $data);
if ($ex[0] == "badchannel") {
$url4 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$ex[1]");
$getchat4 = json_decode($url4, true);
$namech4 = $getchat4["result"]["title"];
$userch4 = $getchat4["result"]["username"];
$id4 = $getchat4["result"]["id"];
$usernames = $update->callback_query->from->username;
$idusers = $update->callback_query->from->id;
$names = $update->callback_query->from->first_name;
$membercall = $update->callback_query->id;
$link4 = $setting[$id4]["link"];
$link4 = trim($link4,"https://t.me/");
bot('answerCallbackQuery',[
   'callback_query_id'=>$update->callback_query->id,
        'text'=>'• تم الابلاغ ❗️',
        
      ]);
for ($d = 0; $d < 5; $d++) {
bot('sendmessage', [
'chat_id' => "$admin[$d]",
'text' => "
• بلاغ جديد على قناة : [$namech4]($link4) ❗️

- ايدي المبلغ : $idusers
- اسم المبلغ : -[$names](t.me/$usernames)",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "اخفاء الابلاغ ", "callback_data" => "h2"]],
[["text" => "الغاء تمويل القناة", "callback_data" => "detm"]]
]
])
]);
}
}
if ($data == "turech") {
$getjoinchannel = $setting[$chat_id2]["getjoinchi"];
for ($i = 0; $i <= count($getjoinchannel); $i++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $getjoinchannel[$i] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel == 'member' or $okchannel == 'creator' or $okchannel == 'administrator') {
$key = array_search("$getjoinchannel[$z]", $setting[$chat_id2]["getjoinchi"]);
$setting[$chat_id2]["turbp"][] = $key;
unset($setting[$chat_id2]["getjoinchi"][$key]);
$setting[$chat_id2]["getjoinchi"] = array_values($setting[$chat_id2]["getjoinchi"]);
file_put_contents("setting.json", json_encode($setting));
$search = array_search($getjoinchannel[$i], $setting["chanel"]);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$i"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$coinchannel = $setting["member"];
$settingnelincoin = $coinchannel[$i];
$downchannel = $settingnelincoin - 1;
if ($downchannel > 0) {
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting["member"]["$i"] = "$downchannel";
$setting["member"] = array_values($setting["member"]);
$setting[$idch]["member"] += 1;
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting[$idch]["member"];
$chhhhhhanel = $setting["chanel"]["$i"];
@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$i"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting["member1"]["$i"];
$chhhhhhanel = $setting["chanel"]["$i"];
$setting[$idch]["member1"] -= 1;
file_put_contents("setting.json", json_encode($setting));
$link = $setting[$idch]["link"];
$member = $setting[$idch]["member"];
$member1 = $setting[$idch]["member1"];
if ($chhhhhhanel != "" and $chhhhhhanel != null) {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• شترك شخص جديد في قناتك : [$namech1](t.me/$userch1)

- العدد المطلوب $member عضو
- العدد المتبقي $member1 عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
$link0 = $setting[$idch]["link"];
$link0 = trim($link0,"https://t.me/");
if ($member1 == "0") {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
for ($d = 0; $d < 5; $d++) {
bot('sendmessage', [
'chat_id' => $admin[$d],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
bot('sendmessage', [
'chat_id' => "$chtm",
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
$allchannel = $setting["chanel"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
}
}
}
$r34 = count($setting[$chat_id2]["turbp"]);
$faes = $pricez * $r34;
$setting[$chat_id2]["coins"] += $faes;
file_put_contents("setting.json", json_encode($setting));
bot("Editmessagetext", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
- <b> • تم اضافة {$faes} نقاط الى حسابك ✅
• بسبب الاشتراك في $r34 قنوات 

- (اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط)</b>",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "التالي", "callback_data" => "turbo"]],
[["text" => "رجوع", "callback_data" => "getcoin"]]
]
])
]);
unset($setting[$chat_id2]["getjoinchi"][$key]);
$setting[$chat_id2]["getjoinchi"] = array_values($setting[$chat_id2]["getjoinchi"]);
file_put_contents("setting.json", json_encode($setting));
if (!in_array($getjoinchannel[$i], $setting["$chat_id2"]["chrubo"])) {
$setting["$chat_id2"]["chrubo"][] = $getjoinchannel[$i];
file_put_contents("setting.json", json_encode($setting, true));
}
}
$allchannel = $setting["chanel"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=$idch");
$jsonlink = json_decode($getlink, true);
$getlinkde = $jsonlink['result'];
if ($userch == null) {
$getlinkde = $jsonlink['result'];
} elseif ($userch != null) {
$getlinkde = "t.me/$userch";
}

if ($data == "noturbo") {
if ($idch == null) {
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "رابط الدعوة ♾", 'callback_data' => 'yourlink']],
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
} else {

bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "• اشترك في القناة : [$namech](tg://openmessage?user_id=$idch)
 
- من ثم اضغط على تحقق لكي تحصل على $pricez نقطه 🌎

• عدد نقاطك الحاليه : $coins",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "$namech", 'url' => "$getlinkde"]],
[['text' => "التالي", 'callback_data' => 'truechannel'], ['text' => "تحقق", 'callback_data' => 'truechannel1']],
[['text' => "ابلاغ", 'callback_data' => 'badchannel']],
[['text' => "•رجوع•", 'callback_data' => 'getcoin']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["cc1"] = $z + 1;
$setting[$chat_id2]["arraychannel"] = $z;
file_put_contents("setting.json", json_encode($setting));
}
}

$arraychannel = $setting[$chat_id2]["arraychannel"];
if ($data == "truechannel1") {
$getjoinchannel = $setting[$chat_id2]["cc3"];
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $getjoinchannel . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
bot('answercallbackquery', [
'callback_query_id' => $update->callback_query->id,
'text' => "
اشترك في القناة اولأ!!",
'show_alert' => true,
]);
} else {
if ($idch != null and $idch != "") {
$arraychannel = $setting[$chat_id2]["arraychannel"];
$coinchannel = $setting["member"];
$settingnelincoin = $coinchannel[$arraychannel];
$downchannel = $settingnelincoin - 1;
if ($downchannel > 0) {
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting["member"]["$arraychannel"] = "$downchannel";
$setting["member"] = array_values($setting["member"]);
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}

@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting["member1"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$setting[$idch]["member1"] -= 1;
file_put_contents("setting.json", json_encode($setting));

$member = $setting[$idch]["member"];
$member1 = $setting[$idch]["member1"];
if ($chhhhhhanel != "" and $chhhhhhanel != null) {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• شترك شخص جديد في قناتك : [$namech1](t.me/$userch1)
 
 - العدد المطلوب $member عضو
 - العدد المتبقي $member1 عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
$allchannel = $setting["chanel"];
@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting[$idch]["member"];
$d1 = $setting["member"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$link0 = $setting[$idch]["link"];
$link0 = trim($link0,"https://t.me/");
if ($member1 == "0") {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
for ($d = 0; $d < 5; $d++) {
bot('sendmessage', [
'chat_id' => $admin[$d],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
bot('sendmessage', [
'chat_id' => "$chtm",
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
if (!in_array($getjoinchannel, $setting["$chat_id2"]["chrubo"])) {
$setting["$chat_id2"]["chrubo"][] = $getjoinchannel;
file_put_contents("setting.json", json_encode($setting, true));
}
$allchannel = $setting["chanel"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$coins = $pricez + $coins;

bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "• اشترك في القناة : [$namech](tg://openmessage?user_id=$idch)
 
- من ثم اضغط على تحقق لكي تحصل على $pricez نقطه 🌎

• عدد نقاطك الحاليه : $coins",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "$namech", 'url' => "$getlinkde"]],
[['text' => "التالي", 'callback_data' => 'truechannel'], ['text' => "تحقق", 'callback_data' => 'truechannel1']],
[['text' => "ابلاغ", 'callback_data' => 'badchannel']],
[['text' => "•رجوع•", 'callback_data' => 'getcoin']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["cc1"] = $z + 1;
$setting[$chat_id2]["arraychannel"] = $z;
$setting[$chat_id2]["coins"] += $pricez;
file_put_contents("setting.json", json_encode($setting));
} else {
$getjoinchannel = $setting[$chat_id2]["cc3"];
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $getjoinchannel . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel == 'member' || $okchannel == 'creator' || $okchannel == 'administrator') {
$arraychannel = $setting[$chat_id2]["arraychannel"];
$coinchannel = $setting["member"];
$settingnelincoin = $coinchannel[$arraychannel];
$downchannel = $settingnelincoin - 1;
if ($downchannel > 0) {
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting["member"]["$arraychannel"] = "$downchannel";
$setting["member"] = array_values($setting["member"]);
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}

@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting["member1"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$setting[$idch]["member1"] -= 1;
file_put_contents("setting.json", json_encode($setting));

$member = $setting[$idch]["member"];
$member1 = $setting[$idch]["member1"];
if ($chhhhhhanel != "" and $chhhhhhanel != null) {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• شترك شخص جديد في قناتك : [$namech1](t.me/$userch1)
 
 - العدد المطلوب $member عضو
 - العدد المتبقي $member1 عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
$allchannel = $setting["chanel"];
@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting[$idch]["member"];
$d1 = $setting["member"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$link0 = $setting[$idch]["link"];
$link0 = trim($link0,"https://t.me/");
if ($member1 == "0") {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
for ($d = 0; $d < 5; $d++) {
bot('sendmessage', [
'chat_id' => $admin[$d],
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
bot('sendmessage', [
'chat_id' => "$chtm",
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
if (!in_array($getjoinchannel, $setting["$chat_id2"]["chrubo"])) {
$setting["$chat_id2"]["chrubo"][] = $getjoinchannel;
file_put_contents("setting.json", json_encode($setting, true));
}
$allchannel = $setting["chanel"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "رابط الدعوة ♾", 'callback_data' => 'yourlink']],
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["cc1"] = $z + 1;
$setting[$chat_id2]["arraychannel"] = $z;
$setting[$chat_id2]["coins"] += $pricez;
file_put_contents("setting.json", json_encode($setting));
}
}
}
}

$cc = $setting[$chat_id2]["cc1"];
$allchannel = $setting["chanel"];

for ($z = $cc; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$cc = $setting[$chat_id2]["cc1"];
for ($z = $cc; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=$idch");
$jsonlink = json_decode($getlink, true);
if ($userch == null) {
$getlinkde = $jsonlink['result'];
} elseif ($userch != null) {
$getlinkde = "t.me/$userch";
}
if ($data == "truechannel") {
if ($idch != null and $idch != "") {
$getjoinchannel = $setting[$chat_id2]["cc3"];
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $getjoinchannel . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' =>
"• اشترك في القناة : [$namech](tg://user?id=$idch)
 
 - من ثم اضغط على تحقق لكي تحصل على $pricez نقطه 🌎
 
 • عدد نقاطك الحاليه : $coins",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "$namech", 'url' => "$getlinkde"]],
[['text' => "التالي", 'callback_data' => 'truechannel'], ['text' => "تحقق", 'callback_data' => 'truechannel1']],
[['text' => "ابلاغ", 'callback_data' => 'badchannel']],
[['text' => "•رجوع•", 'callback_data' => 'getcoin']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["cc1"] = $z + 1;
file_put_contents("setting.json", json_encode($setting));
} else {
if ($idch != null and $idch != "") {
$arraychannel = $setting[$chat_id2]["arraychannel"];
$coinchannel = $setting["member"];
$settingnelincoin = $coinchannel[$arraychannel];
$downchannel = $settingnelincoin - 1;
if ($downchannel > 0) {
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting["member"]["$arraychannel"] = "$downchannel";
$setting["member"] = array_values($setting["member"]);
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}

@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting["member1"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$setting[$idch]["member1"] -= 1;
file_put_contents("setting.json", json_encode($setting));

$member = $setting[$idch]["member"];
$member1 = $setting[$idch]["member1"];
if ($chhhhhhanel != "" and $chhhhhhanel != null) {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• شترك شخص جديد في قناتك : [$namech1](t.me/$userch1)
 
 - العدد المطلوب $member عضو
 - العدد المتبقي $member1 عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
$allchannel = $setting["chanel"];
@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting[$idch]["member"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$link0 = $setting[$idch]["link"];
$link0 = trim($link0,"https://t.me/");
if ($chhhhhhanel == "1") {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• تم نتهاء تمويل قناة : $namech1ب $setmembe3r عضو 🚸 ",
]);
bot('sendmessage', [
'chat_id' => "$chtm",
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
if (!in_array($getjoinchannel, $setting["$chat_id2"]["chrubo"])) {
$setting["$chat_id2"]["chrubo"][] = $getjoinchannel;
file_put_contents("setting.json", json_encode($setting, true));
}
$allchannel = $setting["chanel"];
for ($z = 0; $z <= count($allchannel); $z++) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $allchannel[$z] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
break;
}
}
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$allchannel[$z]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$coins = $pricez + $coins;
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' =>
"• اشترك في القناة : [$namech](tg://user?id=$idch)
 
 - من ثم اضغط على تحقق لكي تحصل على $pricez نقطه 🌎
 
 • عدد نقاطك الحاليه : $coins",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "$namech", 'url' => "$getlinkde"]],
[['text' => "التالي", 'callback_data' => 'truechannel'], ['text' => "تحقق", 'callback_data' => 'truechannel1']],
[['text' => "ابلاغ", 'callback_data' => 'badchannel']],
[['text' => "•رجوع•", 'callback_data' => 'getcoin']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["cc1"] = $z + 1;
$setting[$chat_id2]["coins"] += $pricez;
file_put_contents("setting.json", json_encode($setting));
}
}
} else {
$getjoinchannel = $setting[$chat_id2]["cc3"];
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=" . $getjoinchannel . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel == 'member' || $okchannel == 'creator' || $okchannel == 'administrator') {
$arraychannel = $setting[$chat_id2]["arraychannel"];
$coinchannel = $setting["member"];
$settingnelincoin = $coinchannel[$arraychannel];
$downchannel = $settingnelincoin - 1;
if ($downchannel > 0) {
@$setting = json_decode(file_get_contents("setting.json"), true);
$setting["member"]["$arraychannel"] = "$downchannel";
$setting["member"] = array_values($setting["member"]);
$setting = json_encode($setting, true);
file_put_contents("setting.json", $setting);
}

@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$idch = $getchat1["result"]["id"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting["member1"]["$arraychannel"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$setting[$idch]["member1"] -= 1;
file_put_contents("setting.json", json_encode($setting));

$member = $setting[$idch]["member"];
$member1 = $setting[$idch]["member1"];
if ($chhhhhhanel != "" and $chhhhhhanel != null) {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• شترك شخص جديد في قناتك : [$namech1](t.me/$userch1)
 
 - العدد المطلوب $member عضو
 - العدد المتبقي $member1 عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
}
$allchannel = $setting["chanel"];
@$setting = json_decode(file_get_contents("setting.json"), true);
$url1 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=" . $setting["chanel"]["$arraychannel"] . "");
$getchat1 = json_decode($url1, true);
$namech1 = $getchat1["result"]["title"];
$userch1 = $getchat1["result"]["username"];
$setting = json_decode(file_get_contents("setting.json"), true);
$setmembe3r = $setting[$idch]["member"];
$chhhhhhanel = $setting["chanel"]["$arraychannel"];
$link0 = $setting[$idch]["link"];
$link0 = trim($link0,"https://t.me/");
if ($chhhhhhanel == "1") {
bot('sendmessage', [
'chat_id' => $setting[$idch]["admin"],
'text' => "• تم نتهاء تمويل قناة : $namech1ب $setmembe3r عضو 🚸 ",
]);
bot('sendmessage', [
'chat_id' => "$chtm",
'text' => "• تم نتهاء تمويل قناة : [$namech1](t.me/$link0) ب $setmembe3r عضو 🚸 ",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
]);
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
if (!in_array($getjoinchannel, $setting["$chat_id2"]["chrubo"])) {
$setting["$chat_id2"]["chrubo"][] = $getjoinchannel;
file_put_contents("setting.json", json_encode($setting, true));
}
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "رابط الدعوة ♾", 'callback_data' => 'yourlink']],
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
$setting[$chat_id2]["cc3"] = $idch;
$setting[$chat_id2]["coins"] += $pricez;
file_put_contents("setting.json", json_encode($setting));
} else {
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "رابط الدعوة ♾", 'callback_data' => 'yourlink']],
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
}
}
}

$forward = $message->forward_from_chat;
$forward_id = $message->forward_from_chat->id;
$id1 = $update->message->forward_from->id;
$infos1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$forward_id&user_id=$idBot"), true);
$bot = $infos1['result']['status'];
$can_bot_invite = $infos1['result']['can_invite_users'];
if ($can_bot_invite == 1) {
$can = "✅";
} else {
$can = "❌";
}

if ($forward and $mode == "cdpv") {
if ($can == "✅") {
$max = $setting["$from_id"]["mem"] / $settm;
$maxmember = $setting["$from_id"]["mem"];
$max1 = $settm * $maxmember;
$maxmember1 = floor($max1);
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
• تم خصم ($max1) نقاط
- وبدء تمويل قناتك $maxmember عضو 🚸
<b>
- اذا قمت بطرد البوت من القناة او تنزيله من الادمنيه اثناء التمويل سيتم ستبعاد قناتك من التمويل !!! $id1
</b>
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$forward_id");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$url1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/createChatInviteLink?chat_id=$idch&expire_date=month&member_limit=9999"),1);
$urll = $url1["result"]["invite_link"];
$setting[$idch]["link"] = $urll;
$setting["chanel"][] = $idch;
$setting[$idch]["member1"] = $setting["$from_id"]["mem"];
$setting[$idch]["member"] = $setting["$from_id"]["mem"];
$setting[$idch]["admin"] = "$from_id";
$setting[$from_id]["order"][] = "$idch ";
$setting[$from_id]["mode"] = " ";
$setting[$from_id]["coins"] -= $max1;
file_put_contents("setting.json", json_encode($setting));
$mem = $setting[$from_id]['mem'];
bot("SendMessage", [
"chat_id" => "$admin[1]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
bot("SendMessage", [
"chat_id" => "$admin[0]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
} else {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>• البوت ليس ادمن في قناة</b>",
"reply_to_message_id" => $message_id,
"parse_mode" => "html"
]);
}
}
$infos1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$chat_id&user_id=$idBot"), true);
$bot = $infos1['result']['status'];
$can_bot_invite = $infos1['result']['can_invite_users'];
if ($can_bot_invite == 1) {
$can = "✅";
} else {
$can = "❌";
}
@$statjson = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$chat_id&user_id=" . $from_id), true);
@$status = $statjson['result']['status'];
if ($status == 'creator' or $status == 'administrator') {
if ($text == "تمويل الكروب" and $supergroup) {
if ($can == "✅") {
if ($coa < $coins) {
$max = $coins / $settm;
$maxmember = $max;
$maxmember2 = floor($maxmember);
$max1 = $settm * $maxmember;
$maxmember1 = floor($max1);
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
• تم خصم ($max1) نقاط
- وبدء تمويل قناتك $maxmember2 عضو 🚸
<b>
- اذا قمت بطرد البوت من القناة او تنزيله من الادمنيه اثناء التمويل سيتم ستبعاد قناتك من التمويل !!!
</b>
",
"parse_mode" => "html",
]);
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$chat_id");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$url1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/createChatInviteLink?chat_id=$idch&expire_date=month&member_limit=9999"),1);
$urll = $url1["result"]["invite_link"];
$setting[$idch]["link"] = $urll;
$setting["chanel"][] = $idch;
$setting[$idch]["member1"] = $setting["$from_id"]["mem"];
$setting[$idch]["member"] = $setting["$from_id"]["mem"];
$setting[$idch]["admin"] = "$from_id";
$setting[$from_id]["order"][] = "$idch ";
$setting[$from_id]["mode"] = " ";
$setting[$from_id]["coins"] -= $max1;
file_put_contents("setting.json", json_encode($setting));
$mem = $setting[$from_id]['mem'];
bot("SendMessage", [
"chat_id" => "$admin[1]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
bot("SendMessage", [
"chat_id" => "$admin[0]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
} else {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "• عليك تجميع النقاط ➕💠 اكثر من $coa نقطه !",
"reply_to_message_id" => $message_id,
"parse_mode" => "html"
]);
}
} else {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
<b>• البوت ليس ادمن في قناة</b>",
"parse_mode" => "html"
]);
}
}
}
$infos1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$text&user_id=$idBot"), true);
$bot = $infos1['result']['status'];
$can_bot_invite = $infos1['result']['can_invite_users'];
if ($can_bot_invite == 1) {
$can = "✅";
} else {
$can = "❌";
}
if ($text and $mode == "chgl") {
if ($can == "✅") {
$max = 25 / $settm;
$maxmember = $setting["$from_id"]["mem"];
$max1 = $settm * $maxmember;
$maxmember1 = floor($max1);
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
• تم خصم ($max1) نقاط
- وبدء تمويل قناتك $maxmember عضو 🚸
<b>
- اذا قمت بطرد البوت من القناة او تنزيله من الادمنيه اثناء التمويل سيتم ستبعاد قناتك من التمويل !!!
</b>
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$text");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$url1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/createChatInviteLink?chat_id=$idch&expire_date=month&member_limit=9999"),1);
$urll = $url1["result"]["invite_link"];
$setting[$idch]["link"] = $urll;
$setting["chanel"][] = $idch;
$setting[$idch]["member1"] = $setting["$from_id"]["mem"];
$setting[$idch]["member"] = $setting["$from_id"]["mem"];
$setting[$idch]["admin"] = "$from_id";
$setting[$from_id]["order"][] = "$idch ";
$setting[$chat_id]["mode"] = " ";
$setting[$from_id]["coins"] -= $max1;
file_put_contents("setting.json", json_encode($setting));
$mem = $setting[$from_id]['mem'];
bot("SendMessage", [
"chat_id" => "$admin[1]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
bot("SendMessage", [
"chat_id" => "$admin[0]",
"text" => "
• تم بدء تمويل قناة : [$namech]($urll) | $mem عضو 🚸

- ايدي الشخص : [$from_id]
- اسم شخص : [$name](tg://openmessage?user_id=$from_id)
- عدد نفاط الشخص : $coins",
"parse_mode" => "markdown",
]);
} else {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>• البوت ليس ادمن في قناة</b>",
"reply_to_message_id" => $message_id,
"parse_mode" => "html"
]);
}
}

$coinina = $setting[$chat_id2]["inv"];
$chs = $setting[$chat_id2]["chs"];
$gf = $setting[$chat_id2]["gf"];
$forw = $setting[$chat_id2]["forw"];
if ($data == "yourlink") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "
انسخ الرابط ثم قم بمشاركته مع اصدقائك 📥 .

- كل شخص يقوم بالدخول ستحصل على $priceforward نقطه 📊 .

- بإمكانك عمل اعلان خاص برابط الدعوة ♾ الخاص بك 📬 .

~ رابط الدعوة ♾ :

https://t.me/$userbot?start=$chat_id2

- مشاركتك للرابط : $coinina 🌀
",
'disable_web_page_preview' => 'true',
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]],
]
])
]);
}
if ($data == "infoaccount") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>
• مرحبا بك في 『 للحصول على معلومات حول حسابك ❤️‍🩹 』في بوت التمويل 🌀

- عدد القنوات او المجموعات الجاري تمويلها : 0
- عدد نقاط حسابك : $coins


- عدد عمليات التحويل التي قمت بها : $forw
- عدد القنوات التي شتركت بها : $chs
- عدد الهدايا اليومية التي جمعتها : $gf
- عدد الاعضاء الذي قمت بطلبهم في عمليات التمويل : 0

- عدد مشاركاتك لرابط الدعوة ♾ : $coinina

- المستخدمين الاكثر مشاركة لرابط الدعوى :
</b>
",
'disable_web_page_preview' => 'true', "parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]],
]
])
]);
}

$getjoinchannel = $setting[$chat_id2]["cc3"];
if ($data == "badchannel") {
$url4 = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$getjoinchannel");
$getchat4 = json_decode($url4, true);
$namech4 = $getchat4["result"]["title"];
$userch4 = $getchat4["result"]["username"];
$link4 = $setting[$id4]["link"];
$link4 = trim($link4,"https://t.me/");
$usernames = $update->callback_query->from->username;
$idusers = $update->callback_query->from->id;
$names = $update->callback_query->from->first_name;
$membercall = $update->callback_query->id;
bot('answercallbackquery', [
'callback_query_id' => $membercall,
'text' => "تم ارسال الابلاغ الى مبرمج البوت, وسوف يقوم بمراجعة القناة ومعرفة محتوى القناة ،
نشكرك للتعاون معنا♥️ !",
'show_alert' => true
]);
for ($d = 0; $d < 5; $d++) {
bot('sendmessage', [
'chat_id' => "$admin[$d]",
'text' => "
• بلاغ جديد على قناة : [$namech4]($link4) ❗️

- ايدي المبلغ : $idusers
- اسم المبلغ : -[$names](t.me/$usernames)",
'disable_web_page_preview' => 'true', 'parse_mode' => "Markdown",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "اخفاء الابلاغ ", "callback_data" => "h2"]],
[["text" => "• الغاء التمويل • ", "callback_data" => "detm"]]
]
])
]);
}
}
if ($data == "detm") {
bot('editmessagetext', [
'chat_id' => $chat_id2,
'message_id' => $message_id2,
'text' => "تم حذف القناة من التمويل",
'reply_markup' => json_encode([
'inline_keyboard' => [
[['text' => "•رجوع•", 'callback_data' => 'h2']],
]
])
]);
$arraychannel = $coinchannel - $getjoinchannel;
unset($setting[$idch]["member"]);
$a51 = array_search($idch,$setting["chanel"]);
unset($setting["chanel"]["$a51"]);
unset($setting[$idch]["admin"]);
$setting["chanel"] = array_values($setting["chanel"]);
$setting[$idch]["member"] = array_values($setting[$idch]["member"]);
$setting[$idch]["admin"]= array_values($setting[$idch]["admin"]);
file_put_contents("setting.json", json_encode($setting));
}
$KEYADMIN = json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:$gift50","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:$gift1", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]
]);


if ($text == "/" and in_array($from_id, $admin) and $private) {
$setting["1$chat_id"] = " ";
file_put_contents("setting.json", json_encode($setting));
bot("SendMessage", [
"chat_id" => $chat_id,
"text" =>
"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => $KEYADMIN
]);
}
if ($data == "ongift" and $gift1 != "✅") {
$setting["1$chat_id2"] = " ";
$setting["gift1"] = "✅";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:$gift50","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:✅", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]
])
]);
}
if ($data == "ongift" and $gift1 == "✅") {
$setting["1$chat_id2"] = " ";
$setting["gift1"] = "❌";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:$gift50","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:❌", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]
])
]);
}
$mode = $setting["1$from_id"];
if ($data == "allch") {
$r7j = 0;
$keyboard1 = [];
$order = $setting["chanel"];
foreach ($order as $row) {
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$order[$r7j]");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$mem = $setting["member"];
$d = $setting[$idch]["member"];
$keyboard1["inline_keyboard"][] = [["text" => "$namech", "url" => "t.me/$userch"], ["text" => "$mem[$r7j]/$d", "callback_data" => " "]];
$r7j++;
}
$keyboard1["inline_keyboard"][] = [["text" => "رجوع", "callback_data" => "h1"]];
$order1 = json_encode($keyboard1);
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "هنا جميع القنوات",
"reply_markup" => $order1
]);
}
if ($data == "createlink") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>- حسنا عزيزي ارسل عدد الهدية🦖</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
$setting["1$chat_id2"] = "$data";
file_put_contents("setting.json", json_encode($setting));
}
$rand = substr(str_shuffle("0123456789abcdefghiklmnopqrsuvwxyzABCDEFGHIKLMNOPQRSUVWXYZ"), -18);
if ($text and $mode == "createlink") {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "
• تم خصم $text من عدد نقاطك

- عموله التحويل : $priceforward

• رابط تحويل النقاط : https://t.me/$userbot?start=J$rand

• ارسل الرابط للشخص المراد تحويل النقاط له 

• الرابط صالح لمده 15د

- يمكنك الضغط على زر تعطيل الرابط بعد اقل من 15د لكي تقوم بسترداد عدد نقاطك او قم بدخول على الرابط لاسترداد عدد نقاطك
",
'parse_mode'=>"markdown",
'disable_web_page_preview'=>true,
'reply_to_message_id'=>$message->message_id,
'reply_markup' => json_encode([
"inline_keyboard" => [
[["text" => "تعطيل الرابط", "callback_data" => "breacklink"]],
[["text" => "رجوع", "callback_data" => "h2"]],
]
])
]);
$r = count($settig["forwad"]);
$setting["forward"][$rand]["coin"] = $text;
$setting["forward"][$rand]["niggaa"] = $chat_id;
$setting["forward"][$rand]["count"] = $r;
$setting["forwad"][] = $rand;
$setting[$from_id]["forward"] = " ";
$setting["1$chat_id"] = "";
file_put_contents("setting.json", json_encode($setting));
}
$ex = explode("J", $text);
$d = $setting["forwad"];
if (preg_match("/^\/(start) (J)/s", $text) and $private) {
if (in_array($ex[1], $d)) {
$c = $setting["forward"][$ex[1]]["coin"];
$v = $c + $coins;
$sed = $setting["forward"][$ex[1]]["niggaa"];
$d1 = $setting["forward"][$ex[1]]["count"];
bot('sendmessage', [
'chat_id' => $chat_id,
'text' => "
• تم اضافة $c نقاط الى حسابك ✅
 • بواسطه رابط التحويل من قبل : مالك البوت

 • اصبحت عدد نقاطك$v",
'parse_mode' => "Markdown",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رجوع", "callback_data" => "h2"]]
]
])
]);
$setting[$sed]["forw"] += 1;
$setting[$from_id]["coins"] += $c;
$d1 = array_search($ex[1], $setting["forwad"]);
unset($setting["forwad"][$d1]);
file_put_contents("setting.json", json_encode($setting));
}
}
if ($data == "gift50" and $gift50 != "✅") {
$setting["1$chat_id2"] = " ";
$setting["gift50"] = "✅";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:✅","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:$gift1", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]
])
]);
}
if ($data == "gift50" and $gift50 == "✅") {
$setting["1$chat_id2"] = " ";
$setting["gift50"] = "❌";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
- حساب التواصل: $dev
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text"=>"تعيين حساب المطور","callback_data"=>"setting##dev"]],
[["text"=>"تعيين قناة اثباتات","callback_data"=>"setting##setchs"]],
[["text"=>"هدية تلقائي:❌","callback_data"=>"gift50"],["text"=>"تعيين عدد الهدية التلقائية","callback_data"=>"setting##gift5"]],
[["text" => "تعيين نقاط الدخول", "callback_data" => "setting##setjoincoin"], ["text" => "سعر التمويل", "callback_data" => "setting##settm"]],
[["text" => "تعيين حد ادنى للنقاط", "callback_data" => "setting##coa"]],
[["text" => "تعيين عدد الهدية", "callback_data" => "setting##setgiftcoin"], ["text" => " الهدية:$gift1", "callback_data" => "ongift"]],
[["text" => "تعيين سعر الاشتراك", "callback_data" => "setting##pricez"]],
[["text" => "تعيين سعر عمولة التحويل", "callback_data" => "setting##priceforward"], ["text" => "صنع رابط هدية", "callback_data" => "createlink"]],
[["text" => "اذاعة قناة", "callback_data" => "sendch"]],
[["text" => "اضافة قناة", "callback_data" => "addcn"], ["text" => "مسح كل القنوات", "callback_data" => "delchaw"]],
[["text" => "جميع القنوات", "callback_data" => "allch"]],
]
])
]);
}
if ($data == "addcn") {
$setting["1$chat_id2"] = "addcn";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>- حسنا عزيزي ارسل العدد الان🎡</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
}
if ($text and $mode == "addcn") {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "• قم برفع البوت ادمن في القناة, من ثم تاكد من رفع البوت ادمن بعدها .  ارسل معرف القناه 📬"
]);
$setting["1$chat_id"] = "addcn1";
$setting[$from_id]['mem'] = $text;
file_put_contents("setting.json", json_encode($setting));
}
if ($text and $mode == "addcn1") {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "تم الحفظ"
]);
$url = file_get_contents("https://api.telegram.org/bot$token/getChat?chat_id=$text");
$getchat = json_decode($url, true);
$namech = $getchat["result"]["title"];
$userch = $getchat["result"]["username"];
$idch = $getchat["result"]["id"];
$url1 = json_decode(file_get_contents("https://api.telegram.org/bot$token/createChatInviteLink?chat_id=$idch&expire_date=month&member_limit=9999"),1);
$urll = $url1["result"]["invite_link"];
$setting[$idch]["link"] = $urll;
$setting["chanel"][] = $idch;
$setting[$idch]["member1"] = $setting["$from_id"]["mem"];
$setting[$idch]["member"] = $setting["$from_id"]["mem"];
$setting[$idch]["admin"] = "$from_id";
$setting[$from_id]["order"][] = "$idch ";
$setting[$from_id]["mode"] = " ";
$setting["1$from_id"] = " ";
file_put_contents("setting.json", json_encode($setting));
}
if ($data == "h1") {
$setting["1$chat_id2"] = " ";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" =>
"
- عدد النقاط الدخول :$invite
- عدد نقاط الاشتراك : $pricez
- سعر التمويل : $settm
- عموله التحويل : $priceforward
- ادنى حد للنقاط : $coa
- عدد نقاط الهديه اليوميه :$setgiftcoin

- يمكن للعضو ارسال <code>/id</code> لارسال الايدي الخاص به
",
"parse_mode" => "html",
"reply_markup" => $KEYADMIN
]);
}
if ($data == "sendch") {
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "<b>حسنا عزيزي ارسل القناة</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
$setting["1$chat_id2"] = "sendch";
file_put_contents("setting.json", json_encode($setting));
}
if ($text != "/start" and $mode == "sendch") {
$sddrf = str_replace(["https://t.me/", "t.me/", "@"], ["", "", ""], $text);
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>تم الحفظ \n ارسل عدد النقاط التي سيحصل على العضو من الاشتراك</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
$setting["2$chat_id"] = "$sddrf";
$setting["1$chat_id"] = "sendmem";
file_put_contents("setting.json", json_encode($setting));
}
if ($text != "/start" and $mode == "sendmem") {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>تم الاذاعة</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
$d = $setting["2$chat_id"];
$setting[$d] = "$text";
$setting["1$chat_id"] = "";
file_put_contents("setting.json", json_encode($setting));
$d1 = $setting["user"];
$d12 = $setting["2$chat_id"];
for ($d = 0; $d < count($d1); $d++) {
$getlink = file_get_contents("https://api.telegram.org/bot$token/exportChatInviteLink?chat_id=@$d12");
$jsonlink = json_decode($getlink, true);
$getlinkde = $jsonlink['result'];
bot("SendMessage", [
"chat_id" => $d1[$d],
"text" => "<b>مرحبا عزيزي 🌏</b>
• يمكنك الحصول على $text نقاط مجانا كل ما عليك هو الاشتراك في <a href='t.me/$d12'>القناة</a>ثم الضغط على زر تم الاشتراك",
"parse_mode" => "html",
"reply_markup" => json_encode([
"inline_keyboard" => [
[["text" => "رابط القناة", "url" => "t.me/$d12"]],
[["text" => "تحقق من الاشتراك ✅", "callback_data" => "true##$d12"]]
]
])
]);
}
}
$ex = explode("##", $data);

$d = $setting[$chat_id2]["adch"];
if ($ex[0] == "true") {
if (!in_array("$ex[1]", $d)) {
$getchannel = json_decode(file_get_contents("https://api.telegram.org/bot" . $token . "/getChatMember?chat_id=@" . $ex[1] . "&user_id=" . $chat_id2));
$okchannel = $getchannel->result->status;
if ($okchannel != 'member' && $okchannel != 'creator' && $okchannel != 'administrator') {
bot('answercallbackquery', [
'callback_query_id' => $update->callback_query->id,
'text' => "
اشترك في القناة اولأ 🚦",
'show_alert' => true,
]);
} else {
bot("deletemessage", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
]);
$d = $setting[$ex[1]];
$coins = $coins + $d;
bot("sendmessage", [
"chat_id" => $chat_id2,
"text" => "
<b>
• حصلت على $d نقطة بسبب الاشتراك في القناة 🦾
• ملاحظه : اذا قمت ب مغادره القناة سيتم خصم ضعف النقاط من حسابك 👋

</b>
 اصبحت عدد نقاطك$coins",
"parse_mode" => "html",
]);
$setting["$chat_id2"]["coins"] += $setting[$ex[1]];
$setting["$chat_id2"]["adch"][] = $ex[1];
file_put_contents("setting.json", json_encode($setting));
}
} else {
bot('answercallbackquery', [
'callback_query_id' => $update->callback_query->id,
'text' => "
لقد حصلت على نقاط سابقأ ⚓️",
'show_alert' => true,
]);
}
}


$ex = explode("##", $data);
if ($ex[1] == "setjoincoin") {
$S = "<b>• ارسل عدد النقاط التي يحصل عليها المستخدم من مشاركة الرابط الخاص به 🧩</b>";
} elseif ($ex[1] == "settm") {
$S = "<b>• ارسل عدد النقاط مقابل العضو الواحد 📬</b>";
} elseif ($ex[1] == "coa") {
$S = "<b>• ارسل حد ادنى للنقاط 🎰</b>";
} elseif ($ex[1] == "pricez") {
$S = "<b>• ارسل سعر الاشتراك مقابل القناة الواحدة 🛰</b>";
} elseif ($ex[1] == "priceforward") {
$S = "<b>• ارسل عدد النقاط التي تخصم عند التحويل 📬</b>";
} elseif ($ex[1] == "setgiftcoin") {
$S = "<b>• ارسل عدد النقاط التي يحصل عليها المستخدم من الهدية .</b>";
}
elseif ($ex[1] == "setchs") {
$S = "<b>• قم برفع البوت ادمن في القناة, من ثم تاكد من رفع البوت ادمن بعدها .  ارسل معرف القناه 📬</b>";
}
elseif ($ex[1] == "gift5") {
$S = "<b> • ارسل عدد النقاط التي يحصل عليه العضو الجديد🎗</b>";
}
elseif ($ex[1] == "dev") {
$S = "<b>• ارسال معرف حسابك او بوت تواصل الخاص بك 📬</b>";
}
if ($ex[0] == "setting") {
$setting["1$chat_id2"] = "$ex[1]";
file_put_contents("setting.json", json_encode($setting));
bot("EditMessageText", [
"chat_id" => $chat_id2,
"message_id" => $message_id2,
"text" => "$S",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
}
if ($text and $mode == "setjoincoin" or $mode == "settm" or $mode == "coa" or $mode == "pricez" or $mode == "priceforward" or $mode == "setgiftcoin" or $mode =="setchs" or $mode == "gift5" or $mode == "dev") {
bot("SendMessage", [
"chat_id" => $chat_id,
"text" => "<b>- تم الحفظ ،</b>",
"parse_mode" => "html",
"reply_markup" => $KEYBACK1
]);
$setting["$mode"] = $text;
$setting["1$chat_id"] = " ";
file_put_contents("setting.json", json_encode($setting));
}

