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
import javafx.scene.layout.AnchorPane;
import javafx.stage.DirectoryChooser;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Controller2 implements Initializable{
	  @FXML
	    private Label Menu;
	   @FXML
	    private AnchorPane slider;
	   @FXML
	    private Label MenuClose;

	@FXML
	private TextField txtfield1;
	
	@FXML
	private TextField txtfield2;
	
	String path;
	String Path2,fich_CONVERT;
	public void Select1(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		FileChooser fc = new FileChooser();
		File selectedFile = fc.showOpenDialog(null);
		path = selectedFile.getAbsolutePath();
		txtfield1.setText(selectedFile.getAbsolutePath());
	}
	
	public void Select_fichier_final(ActionEvent e) throws IOException {
		System.setProperty("file.encoding","UTF-8");
		DirectoryChooser fc = new DirectoryChooser();
		File selectedFile = fc.showDialog(null);
		fich_CONVERT = selectedFile.getAbsolutePath();
		txtfield2.setText(selectedFile.getAbsolutePath());
	}
	
	
	@Override
	public void initialize(URL arg0, ResourceBundle arg1) {
		// TODO Auto-generated method stub
		
		 MenuClose.setVisible(false);
		
        slider.setTranslateX(-220);
        Menu.setOnMouseClicked(event -> {
            TranslateTransition slide = new TranslateTransition();
            slide.setDuration(Duration.seconds(0.4));
            slide.setNode(slider);

            slide.setToX(0);
            slide.play();

            slider.setTranslateX(-220);

            slide.setOnFinished((ActionEvent e)-> {
                Menu.setVisible(false);
                MenuClose.setVisible(true);
            });
        });
		
	
		
        MenuClose.setOnMouseClicked(event -> {
            TranslateTransition slide = new TranslateTransition();
            slide.setDuration(Duration.seconds(0.4));
            slide.setNode(slider);

            slide.setToX(-220);
            slide.play();

            slider.setTranslateX(0);

            slide.setOnFinished((ActionEvent e)-> {
                Menu.setVisible(true);
                MenuClose.setVisible(false);
            });
        });
		
		
	}
	
	public void excute(ActionEvent e) throws IOException  {
		
		//***********************************
		
		String arg = ""+txtfield1.getText()+","+txtfield2.getText();
		Path2="tmps\\coddd\\convert_csv.py "+arg ;
		Process p = Runtime.getRuntime().exec("C:\\Python\\Python39\\python.exe "+Path2);
		System.out.println("heeeeeeeeeeeeee");
	}
	private Stage stage;
    private Scene scene;
    private Parent root;
	
	 public void go_to_Conversion(ActionEvent event) throws IOException
	    {
	        Parent root = FXMLLoader.load(getClass().getResource("convertion.fxml"));
	        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
	        scene = new Scene(root);
	        scene.getStylesheets().add(getClass().getResource("st.css").toExternalForm());
	        stage.setScene(scene);
	        stage.show();
	    }
		
	    public void go_to_calcul(ActionEvent event) throws IOException
	    {
	        Parent root = FXMLLoader.load(getClass().getResource("calcul.fxml"));
	        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
	        scene = new Scene(root);
	        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
	        stage.setScene(scene);
	        stage.show();
	    }
		
	    
	    public void go_to_configuration(ActionEvent event) throws IOException
	    {
	        Parent root = FXMLLoader.load(getClass().getResource("inter.fxml"));
	        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
	        scene = new Scene(root);
	        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
	        stage.setScene(scene);
	        stage.show();
	    }
	
	
	
}
