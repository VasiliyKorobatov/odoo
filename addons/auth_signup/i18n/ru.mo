��    2      �  C   <      H    I  �  P  7   K  y   �  ^   �     \  >   |  <   �     �       0        N     V  	   g     q     �  %   �  -   �               (     0     9     H  )   W      �     �     �     �     �  
   �     �            2     8   O  B   �     �     �      �  !        '     3     L     b  
   u  	   �     �     �  G  �  H  �  �  >"  V   �)  �   J*  x   �*  S   i+  �   �+  m   @,  *   �,  
   �,  n   �,     S-  #   j-     �-  K   �-  9   �-  I   -.  �   w.  2   /  *   9/     d/     s/     �/     �/  V   �/  A   0  4   I0     ~0  *   �0  :   �0     �0  0   1  !   G1     i1  q   v1  l   �1  �   U2     �2     3  @   !3  D   b3     �3  $   �3  /   �3  &   4  ,   94     f4     v4     �4                    $   )   &                          2           ,      '      .   !      1              #                                "                     -      +   	             /             (              %   *      0         
    
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <table cellspacing="0" cellpadding="0" style="width:600px;border-collapse:collapse;background:inherit;color:inherit">
        <tbody><tr>
            <td valign="center" width="200" style="padding:10px 10px 10px 5px;font-size: 12px">
                <img src="/logo.png" style="padding: 0px; margin: 0px; height: auto; width: 80px;" alt="${user.company_id.name}">
            </td>
        </tr></tbody>
    </table>
</div>
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <p>Dear ${object.name},</p>
    <p>A password reset was requested for the Odoo account linked to this email.</p>
    <p>You may change your password by following this link which will remain valid during 24 hours:</p>
    <div style="text-align: center; margin-top: 16px;">
        <a href="${object.signup_url}" style="padding: 5px 10px; font-size: 12px; line-height: 18px; color: #FFFFFF; border-color:#875A7B; text-decoration: none; display: inline-block; margin-bottom: 0px; font-weight: 400; text-align: center; vertical-align: middle; cursor: pointer; white-space: nowrap; background-image: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius:3px">Change password</a>
    </div>
    <p>If you do not expect this, you can safely ignore this email.</p>
    <p>Best regards,</p>
</div>
<div style="padding:0px;width:600px;margin:auto; margin-top: 10px; background: #fff repeat top /100%;color:#777777">
    ${user.signature | safe}
    <p style="font-size: 11px; margin-top: 10px;">
        <strong>Sent by ${user.company_id.name} using <a href="www.odoo.com" style="text-decoration:none; color: #875A7B;">Odoo</a></strong>
    </p>
</div> 
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <table cellspacing="0" cellpadding="0" style="width:600px;border-collapse:collapse;background:inherit;color:inherit">
        <tbody><tr>
            <td valign="center" width="200" style="padding:10px 10px 10px 5px;font-size: 12px">
                <img src="/logo.png" style="padding: 0px; margin: 0px; height: auto; width: 80px;" alt="${user.company_id.name}">
            </td>
        </tr></tbody>
    </table>
</div>
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
<p>Dear ${object.name},</p>
    <p>
        You have been invited to connect to "${object.company_id.name}" in order to get access to your documents in Odoo.
    </p>
    <p>
        To accept the invitation, click on the following link:
    </p>
    <div style="text-align: center; margin-top: 16px;">
         <a href="${object.signup_url}" style="padding: 5px 10px; font-size: 12px; line-height: 18px; color: #FFFFFF; border-color:#875A7B; text-decoration: none; display: inline-block; margin-bottom: 0px; font-weight: 400; text-align: center; vertical-align: middle; cursor: pointer; white-space: nowrap; background-image: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius:3px">Accept invitation to "${object.company_id.name}"</a>
    </div>
    <p>Best regards,</p>
</div>
<div style="padding:0px;width:600px;margin:auto; margin-top: 10px; background: #fff repeat top /100%;color:#777777">
    ${user.signature | safe}
    <p style="font-size: 11px; margin-top: 10px;">
        <strong>Sent by ${user.company_id.name} using <a href="www.odoo.com" style="text-decoration:none; color: #875A7B;">Odoo</a></strong>
    </p>
</div> ${object.company_id.name} invitation to connect on Odoo <strong>A password reset has been requested for this user. An email containing the following link has been sent:</strong> <strong>An invitation email containing the following subscription link has been sent:</strong> Allow external users to sign up An email has been sent with credentials to reset your password Another user is already registered using this email address. Authentication Failed. Back to Login Cannot send email: user %s has no email address. Confirm Confirm Password Confirmed Could not create a new account. Could not reset your password Enable password reset from Login page If unchecked, only invited users may sign up. Invalid signup token Never Connected Partner Password Password reset Reset Password Reset password: invalid username or email Send Reset Password Instructions Send an Invitation Email Sign up Signup Token Type Signup Token is Valid Signup URL Signup expiration Signup token Status Template user for new users created through signup The full URL to access the document through the website. This allows users to trigger a password reset from the Login page. Users Visible in Website Website Partner Full Description Website Partner Short Description Website URL Website meta description Website meta keywords Website meta title Your Email Your Name base.config.settings e.g. John Doe Project-Id-Version: Odoo Server 10.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2016-10-10 08:43+0000
PO-Revision-Date: 2017-07-11 13:24+0500
Last-Translator: Korobarov Vasiliy <korobarov@akvastil.com>
Language-Team: Russian (https://www.transifex.com/odoo/teams/41243/ru/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: ru
Plural-Forms: nplurals=4; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<12 || n%100>14) ? 1 : n%10==0 || (n%10>=5 && n%10<=9) || (n%100>=11 && n%100<=14)? 2 : 3);
X-Generator: Poedit 2.0.2
 
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <table cellspacing="0" cellpadding="0" style="width:600px;border-collapse:collapse;background:inherit;color:inherit">
        <tbody><tr>
            <td valign="center" width="200" style="padding:10px 10px 10px 5px;font-size: 12px">
                <img src="/logo.png" style="padding: 0px; margin: 0px; height: auto; width: 80px;" alt="${user.company_id.name}">
            </td>
        </tr></tbody>
    </table>
</div>
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <p>Дорогой ${object.name},</p>
    <p>Был запрошен сброс пароля для учетной записи Odoo, связанной с этим электронным письмом.</p>
    <p>Вы можете изменить свой пароль, перейдя по этой ссылке, которая останется действительной в течение 24 часов:</p>
    <div style="text-align: center; margin-top: 16px;">
        <a href="${object.signup_url}" style="padding: 5px 10px; font-size: 12px; line-height: 18px; color: #FFFFFF; border-color:#875A7B; text-decoration: none; display: inline-block; margin-bottom: 0px; font-weight: 400; text-align: center; vertical-align: middle; cursor: pointer; white-space: nowrap; background-image: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius:3px">Изменить пароль</a>
    </div>
    <p>Если вы не ожидаете этого, можете смело игнорировать это письмо.</p>
    <p>С наилучшими пожеланиями,</p>
</div>
<div style="padding:0px;width:600px;margin:auto; margin-top: 10px; background: #fff repeat top /100%;color:#777777">
    ${user.signature | safe}
    <p style="font-size: 11px; margin-top: 10px;">
        <strong>Отправлено от ${user.company_id.name} using <a href="www.odoo.com" style="text-decoration:none; color: #875A7B;">Odoo</a></strong>
    </p>
</div> 
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
    <table cellspacing="0" cellpadding="0" style="width:600px;border-collapse:collapse;background:inherit;color:inherit">
        <tbody><tr>
            <td valign="center" width="200" style="padding:10px 10px 10px 5px;font-size: 12px">
                <img src="/logo.png" style="padding: 0px; margin: 0px; height: auto; width: 80px;" alt="${user.company_id.name}">
            </td>
        </tr></tbody>
    </table>
</div>
<div style="padding:0px;width:600px;margin:auto;background: #FFFFFF repeat top /100%;color:#777777">
<p>Дорогой ${object.name},</p>
    <p>
        Вам было предложено подключиться к "${object.company_id.name}" чтобы получить доступ к вашим документам в Odoo.
    </p>
    <p>
        Чтобы принять приглашение, нажмите следующую ссылку:
    </p>
    <div style="text-align: center; margin-top: 16px;">
         <a href="${object.signup_url}" style="padding: 5px 10px; font-size: 12px; line-height: 18px; color: #FFFFFF; border-color:#875A7B; text-decoration: none; display: inline-block; margin-bottom: 0px; font-weight: 400; text-align: center; vertical-align: middle; cursor: pointer; white-space: nowrap; background-image: none; background-color: #875A7B; border: 1px solid #875A7B; border-radius:3px">Принять приглашение "${object.company_id.name}"</a>
    </div>
    <p>С наилучшими пожеланиями,</p>
</div>
<div style="padding:0px;width:600px;margin:auto; margin-top: 10px; background: #fff repeat top /100%;color:#777777">
    ${user.signature | safe}
    <p style="font-size: 11px; margin-top: 10px;">
        <strong>Отправлено от ${user.company_id.name} using <a href="www.odoo.com" style="text-decoration:none; color: #875A7B;">Odoo</a></strong>
    </p>
</div> ${object.company_id.name} приглашение для подключения к Odoo <strong>Пользователь запросил сброс пароля. Отправлено email, содержащее следующую ссылку:</strong> <strong>Отправлено email, содержащее следующую ссылку с подпиской:</strong> Разрешить регистрацию внешним пользователям На указанный адрес было выслано письмо с инструкциями по сбросу пароля Другой пользователь уже зарегистрирован с этим адресом email. Ошибка аутентификации. Войти Невозможно отправить email: пользователь %s не имеет адреса email. Подтвердить Подтвердите пароль Подтверждено Невозможно создать новую учетную запись. Невозможно сбросить Ваш пароль Включить сброс пароля со страницы входа Если не отмечено, только приглашенные пользователи могут зарегистрироваться Неверный токен регистрации Никогда не подключался Партнёр Пароль Сброс пароля Сброс пароля Сброс пароля: неверное имя пользователя или email Отправить инструкцию Сброса Пароля Отправить Email с приглашением Регистрация Тип токена регистрации Токен регистрации действителен URL регистрации Срок действия регистрации Токен регистрации Статус Шаблон новых пользователей, созданных в процессе регистрации Полный URL, чтобы получить доступ к документу через веб-сайт. Это позволяет пользователям запросить сброс пароля со страницы входа в систему. Пользователи Видимый на сайте Полное описание партнера веб-сайта Короткое описание партнера веб-сайта URL веб-сайта Мета описание сайта Мета-ключевые слова сайта Мета заголовок сайта Адрес электронной почты Ваше Имя base.config.settings напр. ФИО 