
## 安装步骤 
```
sudo apt-get install mysql-server

sudo mysql_secure_installation

sudo systemctl restart mysql
```
## 操作步骤
```
python3 -m flask db init
```


### 如果提示错误可以看看这些：

在您提供的输出中，有几个关键点需要注意：

VALIDATE PASSWORD 组件：MySQL 提供了一个密码验证组件，用于确保用户设置的密码足够安全。当您安装 MySQL 时，它可能会询问您是否要设置这个组件。在您的情况下，系统询问了您，您选择了“No”（通过输入“n”）。这意味着密码强度不会由系统自动验证。如果您后来想要启用这个功能，您可以在 MySQL 中手动配置。

使用 auth_socket 插件：输出中提到“Skipping password set for root as authentication with auth_socket is used by default.” 这意味着 root 用户默认使用 auth_socket 插件进行身份验证，而不是密码。auth_socket 插件在本地系统上通过 Unix 套接字文件来验证用户，这意味着对 MySQL 的访问将限于具有操作系统级别访问权限的用户。在这种情况下，root 用户在 MySQL 中的访问权限与他们在操作系统中的 root 用户身份相关联。

这种配置在某些环境中是安全的，因为它防止了通过网络进行的未授权访问尝试。但是，这也意味着您不能仅通过提供密码来远程或以非 root 操作系统用户身份登录 MySQL root 用户。如果您需要以不同的方式验证，例如通过密码，您需要更改 root 用户的身份验证方法。

如果您想要将 root 用户的身份验证方法更改为密码验证，您可以按照以下步骤操作：

登录到 MySQL（由于您当前使用的是 auth_socket，您可能需要以操作系统 root 用户身份执行此操作）。

更改 root 用户的身份验证方法并设置密码：

sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'your_secure_password';  
FLUSH PRIVILEGES;
将 'your_secure_password' 替换为您选择的安全密码。

退出 MySQL 并重启服务以使更改生效。

请注意，更改身份验证方法可能会影响到系统的安全性，因此在做出此类更改之前，请确保您了解潜在的影响，并根据您的安全需求进行评估。

在这之后登陆  sudo mysql -u root -p 即可