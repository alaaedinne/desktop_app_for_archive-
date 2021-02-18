from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.uic import loadUiType
import sys
import sqlite3
import datetime 
from PyQt5.QtCore import QDate,Qt
from dateutil.parser import parse


MainUI,_ = loadUiType('form_archive.ui')

class Main(QMainWindow , MainUI):
    def __init__(self , parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.UI_Changes()
        self.connect_db()
        self.Show_all_users()
        self.Edit_key()
        self.complete_name()
######################################
    #####################################################
    
    def open_tous_tab(self):
        self.tabWidget_2.setCurrentIndex(0)
        self.Show_all_users()
        self.lineEdit.clear()
        self.statusBar().showMessage("")
    def open_add_tab(self):
        self.tabWidget_2.setCurrentIndex(1)
        self.statusBar().showMessage("")
    def open_Edit_tab(self):
        self.tabWidget_2.setCurrentIndex(2)
        self.statusBar().showMessage("")
        self.lineEdit_13.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_8.clear()
        self.lineEdit_12.clear()
        self.lineEdit_9.clear()
        self.lineEdit_14.clear()
    def open_settings_tab(self):
        self.tabWidget_2.setCurrentIndex(3)
        self.statusBar().showMessage("")
    #########################################################""

    def UI_Changes(self):
    ##UI Changes in log in
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget.tabBar().setVisible(False)
        self.groupBox_7.setVisible(False)
        self.groupBox_8.setVisible(False)
        pass

    ################################################################################
    #####################################################""
    ######## "data base connection" #######################
    
    
    def connect_db(self):
        ## Connection between app and Db
        self.db = sqlite3.connect(database='archive.db')
        self.cur = self.db.cursor()
        print("cnx accepted")


    #######################################################################
    ##################################################################""


    def Handel_Buttons(self):
    # handeel all button of app
        try : 
            self.pushButton.clicked.connect(self.open_tous_tab)
            self.pushButton_2.clicked.connect(self.open_add_tab)
            self.pushButton_4.clicked.connect(self.open_Edit_tab)
            self.pushButton_5.clicked.connect(self.open_settings_tab)

            self.pushButton_6.clicked.connect(self.Add_new_users)
            self.pushButton_8.clicked.connect(self.Edit_user_search)
            self.pushButton_7.clicked.connect(self.Edit_user)
            self.pushButton_12.clicked.connect(self.Delete_user)
            self.pushButton_3.clicked.connect(self.search_all_users)


            self.pushButton_14.clicked.connect(self.Add_information_systeme)

            self.pushButton_10.clicked.connect(self.Edit_key)
            self.pushButton_9.clicked.connect(self.Edit_password)

            self.pushButton_43.clicked.connect(self.Log_in)
            self.pushButton_42.clicked.connect(self.Go_to_reset_password)
            self.pushButton_11.clicked.connect(self.reset_password)

            self.pushButton_13.clicked.connect(self.alert)
            self.pushButton_15.clicked.connect(self.retoure)
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
    ##################################################################
    ##########################################################""
  
    def Add_new_users(self):
        #add user information
        name = self.lineEdit_2.text()
        full_name = self.lineEdit_3.text()
        code = self.lineEdit_4.text()
        date = self.dateEdit.date()
        casie = self.lineEdit_5.text()
        row = self.lineEdit_6.text()
        col = self.lineEdit_7.text()

        try:
            if name != "" :
                print(date.toString(Qt.ISODate))
                self.cur.execute('''
                    INSERT INTO Users(nom, prenom, matriculle,date_dexp,  casie, row, col)
                    VALUES ('%s','%s','%s','%s','%s','%s','%s')
                    '''%(name, full_name, code,date.toString(Qt.ISODate), casie, row, col ))            
                self.db.commit()
                print('donne')
                self.Show_all_users()
                self.statusBar().showMessage("operation avec succéé")
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()

            else: 
                print('ecrire le nom svp')
                self.statusBar().showMessage("ecrire le nom svp")

        except : 
            self.statusBar().showMessage("Erreur,ce matriculle definie déja")
##########################################################################################F"
#########################################################################################""""


    def Show_all_users(self):
        try :
            self.tableWidget.setRowCount(0) 
            self.tableWidget.insertRow(0)
            self.cur.execute('''
                SELECT matriculle, nom ,prenom ,casie ,row ,col ,date_dexp FROM Users 
            ''')
            data = self.cur.fetchall()
            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget.setItem( row, col, QTableWidgetItem(item))
                    col+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")

    ################################# SERCH FOR ALL #############################################################

    def search_all_users(self):
        try:
            name = self.lineEdit.text()
            self.cur.execute(''' 
                SELECT matriculle, nom ,prenom ,casie ,row ,col ,date_dexp FROM Users WHERE nom='%s'
                '''%(name))
            data = self.cur.fetchall()
            print(data)
            self.tableWidget.setRowCount(0) 
            self.tableWidget.insertRow(0)
            for row , form in enumerate(data):
                for col , item in enumerate(form):
                    self.tableWidget.setItem( row, col, QTableWidgetItem(item))
                    col+=1
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)

        except: 
            print('ereur')


###################################################################################################
    def complete_name(self):
        self.cur.execute('''
            SELECT nom FROM Users
            ''')
        names = self.cur.fetchall()
        for name in names:
            print(name)
            completer = QCompleter( name[0] )
            self.lineEdit.setCompleter(completer)
###############################################################################################""

    def Edit_user_search(self):
        try : 
            user_matriculle = self.lineEdit_14.text()
            if user_matriculle != "" :
                SQlite = ('''
                    SELECT * FROM Users WHERE matriculle = '%s'
                ''')
                self.cur.execute(SQlite %(user_matriculle))
                data= self.cur.fetchone()
                print(data)

                
                self.lineEdit_13.setText(data[1])
                self.lineEdit_10.setText(data[2])
                self.lineEdit_11.setText(data[3])
                self.lineEdit_8.setText(data[5])
                self.lineEdit_12.setText(data[6])
                self.lineEdit_9.setText(data[7])
            else:
                self.statusBar().showMessage("Ecrire un matriculle svp")
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
#############################################################################################"

    def Edit_user(self):
        #Edit user information
        try: 
            name = self.lineEdit_13.text()
            full_name = self.lineEdit_10.text()
            code = self.lineEdit_11.text()
            casie = self.lineEdit_8.text()
            row = self.lineEdit_12.text()
            col = self.lineEdit_9.text()

            if name != "" : 
                self.cur.execute('''
                    UPDATE Users SET nom='%s' , prenom='%s' , matriculle='%s' , casie='%s' , row='%s' , col='%s' WHERE matriculle = '%s'
                    '''%(name, full_name, code, casie, row, col , code))

                self.db.commit()
                print('donne edit')        
                self.Show_all_users()
                self.statusBar().showMessage("operation avec succéé")
                self.lineEdit_13.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()
                self.lineEdit_8.clear()
                self.lineEdit_12.clear()
                self.lineEdit_9.clear()
                self.lineEdit_14.clear()
            else: 
                self.statusBar().showMessage("Ecrire un matriculle svp")
        except : 
            self.statusBar().showMessage("Erreur...")
        
    #################################################################################################

    def Delete_user(self):
        #delete user information 
        user_matriculle = self.lineEdit_14.text()
        try : 
            if user_matriculle != "":
                delete_massage= QMessageBox.warning(self, "supprimer" , "Êtes-vous sûr de supprimer les informations", QMessageBox.Yes | QMessageBox.No) 

                
                if delete_massage == QMessageBox.Yes and user_matriculle != "" :
                    sql = (''' 
                        DELETE FROM Users WHERE matriculle = '%s'
                    ''')
                    self.cur.execute(sql %(user_matriculle))
                    self.db.commit()
                    self.statusBar().showMessage("operation avec succéé")
                    self.Show_all_users()
                else : 
                    self.statusBar.showMessage("Remplir le champ svp")
            else: 
                self.statusBar().showMessage("Ecrire un matriculle svp")
        except : 
            self.statusBar().showMessage("Erreur...")
######################################################################################

    def alert(self):
        self.cur.execute('''
            SELECT date_dexp FROM Users
        ''')

        date_array = self.cur.fetchall()
        print(date_array)
        


        
      

        CurrentDate = datetime.date.today()
        print(CurrentDate)
        
        try: 
            for date in date_array :

                dt = parse(date[0])
                print(dt.date())

                self.cur.execute('''
                    SELECT nom ,prenom,matriculle ,casie ,row ,col FROM Users WHERE date_dexp= '%s'
                '''%(date[0]))

                global_data = self.cur.fetchone()
                print(global_data)
                nom= global_data[0]
                prenom = global_data[1]
                matricul = global_data[2]
                casie = global_data[3]
                row = global_data[4]
                col = global_data[5]

                if dt.date() <= CurrentDate :

                    delete_massage= QMessageBox.warning(self, "Expiration" , f"le dossier de {nom} {prenom} qui attacher de ce matriculle {matricul} est expirer le : {dt.date()} le dossier dans le casie : {casie} a la ligne : {row} et la colonne : {col}  "  , QMessageBox.Yes ) 
                    if delete_massage == QMessageBox.Yes:
                        sql = ('''
                            DELETE FROM Users WHERE date_dexp = '%s'
                            ''')
                        self.cur.execute(sql %(date))
                        self.db.commit()
                        print('delete')
                        #self.tabWidget_2.setCurrentIndex(2)
                        self.Show_all_users()
                    
                else :
                    self.statusBar().showMessage("Consiel : supprimé le dossier qui dépasse les limittes.")
                            
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
    
##############################################################################################################################################
        ##########################################################################################################################"
            # ###########################################################################################################
                    ###############################################################################################


    def Add_information_systeme(self):

        username = self.lineEdit_24.text()
        password = self.lineEdit_25.text()
        key = self.lineEdit_26.text()

        try: 
            self.cur.execute('''
                INSERT INTO Info__systeme(username , password , key)
                VALUES ('%s', '%s', '%s')
                '''%(username , password , key))

            self.db.commit()
            print('informatin entrer')
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")

    ##############################################################################################
    ##########################  SETTINGS   #######################################################
    def Edit_key(self): 
        new_key = self.lineEdit_20.text()
        password = self.lineEdit_21.text()

        try : 
            self.cur.execute('''
                SELECT password FROM Info__systeme
                ''')

            data = self.cur.fetchone()

            print(data[0])
            if password == data[0] : 
                self.cur.execute('''
                    UPDATE Info__systeme SET key= '%s' WHERE key = '%s'
                    '''%(new_key , new_key))
                self.db.commit()
                print('donne edit key')
                self.statusBar().showMessage("le nom de recupèration est modifier avec succèes ")
                self.lineEdit_20.clear()
                self.lineEdit_21.clear()
            
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
###########################################################################################""

    def Edit_password(self):
        current_password = self.lineEdit_15.text()
        new_password = self.lineEdit_16.text()
        new_password_2 = self.lineEdit_17.text()
        key = self.lineEdit_18.text()

        try: 
            self.cur.execute('''
                SELECT password FROM Info__systeme
                ''')

            data = self.cur.fetchone()


            self.cur.execute('''
                SELECT key FROM Info__systeme
                ''')

            inf = self.cur.fetchone()

            if current_password == data[0] and new_password == new_password_2 and key == inf[0] : 

                self.cur.execute('''
                    UPDATE Info__systeme SET password = '%s' WHERE key = '%s'
                    '''%(new_password , key))
                self.db.commit()
                print('donne edit password')
                self.statusBar().showMessage("le mot de passe est modifier avec succèes ")
                self.lineEdit_15.clear()
                self.lineEdit_16.clear()
                self.lineEdit_17.clear()
                self.lineEdit_18.clear()
            else: 
                print('problem')
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
    ###############################################################################################################
    ############################## LOG IN PAGE #####################################################################

    def Log_in(self):
        username = self.lineEdit_48.text()
        password = self.lineEdit_49.text()

        try : 
            self.cur.execute('''
                SELECT password FROM Info__systeme
                ''')

            data = self.cur.fetchone()


            self.cur.execute('''
                SELECT username FROM Info__systeme
                ''')

            inf = self.cur.fetchone()

            if data[0] == password and inf[0] == username :
                self.tabWidget.setCurrentIndex(2) 
            else :
                self.groupBox_7.setVisible(True) 
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")
############################################################################################################
    def Go_to_reset_password(self):
        self.tabWidget.setCurrentIndex(1)

############################################################################################################
############################### RESET PASSWORD PAGE ######################################################

    def reset_password(self):
        key = self.lineEdit_19.text()
        new_password_x = self.lineEdit_22.text()
        new_password_y = self.lineEdit_23.text()
        self.cur.execute('''
            SELECT key FROM Info__systeme
            ''')

        result = self.cur.fetchone()

        try:
            if result[0]== key and new_password_x == new_password_y :
                self.cur.execute('''
                    UPDATE Info__systeme SET password = '%s' WHERE key = '%s'
                    '''%(new_password_x , key))
                self.db.commit()
                print('donne edit password succefly')
                self.tabWidget.setCurrentIndex(2)
            else: 
                self.groupBox_8.setVisible(True)
                self.statusBar().showMessage("Erreur,si vous besoin d'aide contacter le dèvlopeur : 0658118268 .")
        except : 
            self.statusBar().showMessage("Erreur, declaré le problème par email : dehganuss@gmail.com ou contacter moi : 0658118268 .")

    ##############################################################################################################
    def retoure(self):
        self.tabWidget.setCurrentIndex(0)
 
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()