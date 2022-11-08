package application;

import java.io.IOException;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.image.Image;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;





import java.net.URL;
import java.util.ResourceBundle;

import javafx.animation.TranslateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Controller_main implements Initializable {

	
	@FXML
    private AnchorPane slider;

    @FXML
    private Label Menu;

    @FXML
    private Label MenuClose;

	
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

	
	
	
	//*****************nav ***************
	/*
	public void go_to_conversion(ActionEvent e) throws IOException {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("conversion.fxml"));
		    Scene scene = new Scene(root); 
		    Scene2FxmlDocumentcontroller
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}*/
	
	private Stage stage;
    private Scene scene;
    private Parent root;
	
    public void go_to_Conversion(ActionEvent event) throws IOException
    {
        Parent root = FXMLLoader.load(getClass().getResource("convertion.fxml"));
        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        Image icon =new Image ("USTHB_Logo.png");
        stage.getIcons().add(icon) ;
        scene.getStylesheets().add(getClass().getResource("st.css").toExternalForm());
        stage.setScene(scene);
        stage.show();
    }
	
    public void go_to_calcul(ActionEvent event) throws IOException
    {
        Parent root = FXMLLoader.load(getClass().getResource("calcul.fxml"));
        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        Image icon =new Image ("USTHB_Logo.png");
        stage.getIcons().add(icon) ;
        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
        stage.setScene(scene);
        stage.show();
    }
	
    
    public void go_to_configuration(ActionEvent event) throws IOException
    {
        Parent root = FXMLLoader.load(getClass().getResource("inter.fxml"));
        stage =(Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        Image icon =new Image ("USTHB_Logo.png");
        stage.getIcons().add(icon) ;
        scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
        stage.setScene(scene);
        stage.show();
    }
    
    
	
}
