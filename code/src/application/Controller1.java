package application;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.animation.TranslateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.DirectoryChooser;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Controller1 implements Initializable {
	
	@FXML
	private TextField txtfield1;
	@FXML
	private TextField txtfield2;
	@FXML
	private TextField txtfield3;
	@FXML
	private TextField txtfield4;
	
	
	
	@FXML
	private TextField txtfield5;
	@FXML
	private TextField txtfield6;
	@FXML
	private TextField txtfield7;
	@FXML
	private TextField txtfield8;
	
	
	@FXML
	private TextField txtfield9;
	@FXML
	private TextField txtfield10;
	@FXML
	private TextField txtfield11;
	@FXML
	private TextField txtfield12;
	
	
	
	@FXML
	private ChoiceBox<String> mychoiceBox;
	@FXML
	private ChoiceBox<String> mychoiceBox2;
	
	private String[] mois= {"1","2","3","4","5","6" };
	
	
	
	@FXML
	private TextField fichier_final;
	
	// nombre de semaine dans le S1 por chaque moi
	@FXML
	private TextField S1_moi1;
	@FXML
	private TextField S1_moi2;
	@FXML
	private TextField S1_moi3;
	@FXML
	private TextField S1_moi4;
	@FXML
	private TextField S1_moi5;
	@FXML
	private TextField S1_moi6;
	
	// nombre de semaine dans le S2 por chaque moi
	@FXML
	private TextField S2_moi1;
	@FXML
	private TextField S2_moi2;
	@FXML
	private TextField S2_moi3;
	@FXML
	private TextField S2_moi4;
	@FXML
	private TextField S2_moi5;
	@FXML
	private TextField S2_moi6;
	
	@FXML
    private Label MenuClose;
	
	String path;
	String fich_org_s1,fich_org_s2;
	String sheet_org_s1,sheet_org_s2;
	String fich_mosul_s1,fich_mosul_s2;
	String  sheet_mosul_s1,sheet_mosul_s2 ;
	String fich_final;
	String  charge_max,heur_supp_max;
	String arg,Path2,reliqaut ;
	
	
	
	public void Select1(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		fich_org_s1 = selectedFile.getAbsolutePath();
		txtfield1.setText(selectedFile.getAbsolutePath());
	}
	public void Select2(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		fich_org_s2 = selectedFile.getAbsolutePath();
		txtfield2.setText(selectedFile.getAbsolutePath());
	}
	public void Select3(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		fich_mosul_s1 = selectedFile.getAbsolutePath();
		txtfield3.setText(selectedFile.getAbsolutePath());
	}
	public void Select4(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		fich_mosul_s2 = selectedFile.getAbsolutePath();
		txtfield4.setText(selectedFile.getAbsolutePath());
	}
	
	public void Select_fichier_final(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		DirectoryChooser fc = new DirectoryChooser();
		File selectedFile = fc.showDialog(null);
		fich_final = selectedFile.getAbsolutePath();
		fichier_final.setText(selectedFile.getAbsolutePath());
	}
	
	@Override
	public void initialize(URL arg0, ResourceBundle arg1) {
		txtfield1.setDisable(true);
		// TODO Auto-generated method stub
		mychoiceBox.getItems().addAll(mois);
		mychoiceBox2.getItems().addAll(mois);
	}
	
	public void Select_reliquat(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		reliqaut = selectedFile.getAbsolutePath();
		txtfield11.setText(selectedFile.getAbsolutePath());
	}
	
	public void excute(ActionEvent e) throws IOException  {
		sheet_org_s1=txtfield5.getText();
		sheet_org_s2=txtfield6.getText();
		sheet_mosul_s1=txtfield7.getText();
		sheet_mosul_s2=txtfield8.getText();
		charge_max=txtfield9.getText();
		heur_supp_max=txtfield10.getText();
		//***********************************
		
		arg=""+fich_org_s1+","+sheet_org_s1+","+fich_org_s2+","+sheet_org_s2+","+fich_mosul_s1+","+sheet_mosul_s1+","+fich_mosul_s2+","+sheet_mosul_s2+","+fich_final+","+charge_max+","+heur_supp_max+","
		+S1_moi1.getText()+","+S1_moi2.getText()+","+S1_moi3.getText()+","+S1_moi4.getText()+","+S1_moi5.getText()+","+S1_moi6.getText()+","	
		+S2_moi1.getText()+","+S2_moi2.getText()+","+S2_moi3.getText()+","+S2_moi4.getText()+","+S2_moi5.getText()+","+S2_moi6.getText()+","+reliqaut+","+txtfield12.getText();
		System.out.println(arg);
		Path2="tmps\\coddd\\cree_json.py "+arg ;
		Process p = Runtime.getRuntime().exec("C:\\Python\\Python39\\python.exe "+Path2);
		System.out.println("heeeeeeeeeeeeee");
	}    
	
	private Stage stage;
    private Scene scene;
    private Parent root;
	
	 public void go_to_main(ActionEvent event) throws IOException
	    {
	        Parent root = FXMLLoader.load(getClass().getResource("main.fxml"));
	        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
	        scene = new Scene(root);
	        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
	        stage.setScene(scene);
	        stage.show();
	    }
}
