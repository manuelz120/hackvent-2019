VERSION 5.00
Begin VB.Form Form1
  Caption = "HACKVent 2019 - Back to Basic"
  ScaleMode = 1
  AutoRedraw = False
  FontTransparent = True
  'Icon = n/a
  LinkTopic = "Form1"
  ClientLeft = 60
  ClientTop = 450
  ClientWidth = 5040
  ClientHeight = 2475
  StartUpPosition = 2 'CenterScreen
  Begin TextBox Text1
    Left = 600
    Top = 840
    Width = 3735
    Height = 285
    Text = "HV19"
    TabIndex = 0
    Alignment = 2 'Center
  End
  Begin Label Label1
    Left = 600
    Top = 1560
    Width = 3735
    Height = 255
    Enabled = 0   'False
    TabIndex = 1
    Alignment = 2 'Center
  End
End

Attribute VB_Name = "Form1"



Private Sub Form_Load() '401DD0
  loc_00401E3B: Text1.Text = "insert your flag here"
  loc_00401E79: Text1.SelStart = 0
  loc_00401ECB: var_18 = Text1.Text
  loc_00401EF7: Text1.SelLength = Len(var_18)
  loc_00401F3D: GoTo loc_00401F5C
  loc_00401F5B: Exit Sub
  loc_00401F5C: 'Referenced from: 00401F3D
End Sub

Private Sub Text1_Change() '401F80
  Dim var_4C As TextBox
  loc_00402072: ref_to_text = Text1.Text
  loc_004020A6: ref_to_text2 = ref_to_text
  ' check if HV19 is at beginning
  loc_00402228: var_ret_7 = (Mid(ref_to_text2, 1, 1) = &H401B20) And (Mid(ref_to_text2, 2, 1) = &H401B28) And (Mid(ref_to_text2, 3, 1) = &H401B30) And (Mid(ref_to_text2, 4, 1) = &H401B38)
  loc_00402235: starts_with_hv19 = CBool(var_ret_7)
  loc_00402280: If starts_with_hv19 = 0 Then GoTo loc_004024B2
  loc_004022A2: flag_length = Len(ref_to_text2)
  loc_004022B9: If (flag_length = 33) = 0 Then GoTo loc_00402486



  loc_0040232D: For loop_counter = 6 To Len(ref_to_text2) - 1 Step 1
  next_iteration: 
  loc_0040233B: If var_1D4 = 0 Then GoTo after_loop
  loc_00402375: var_154 = Asc(CStr(Mid(ref_to_text2, CLng(loop_counter), 1)))
  loc_00402391: call Xor(var_7C, var_15C, loop_counter, var_4C, Me, Me, %S_eax_S = CLng(%StkVar1), %x1 = Mid(%StkVar2, %StkVar3, %StkVar4), 00000002h)
  loc_00402398: var_ret_A = CLng(Xor(var_7C, var_15C, loop_counter, var_4C, Me, Me, var_ret_A = CLng(%StkVar1), %x1 = Mid(%StkVar2, %StkVar3, %StkVar4), 00000002h))
  loc_004023C5: var_44 = var_44 + Chr(var_ret_A)

  loc_00402400: Next loop_counter
  loc_00402406: GoTo next_iteration


  after_loop: 'Referenced from: 0040233B
  loc_00402433: If (var_44 = "6klzic<=bPBtdvff'yFI" = 0 Then GoTo loc_00402477
  loc_00402456: var_eax = Unknown_VTable_Call[ecx+00000054h]
  loc_00402477: 'Referenced from: 00402433
  loc_00402481: GoTo loc_00402574
  loc_00402486: 'Referenced from: 004022B9
  loc_004024A7: var_eax = Unknown_VTable_Call[ecx+00000054h]
  loc_004024AE: If Unknown_VTable_Call[ecx+00000054h] >= 0 Then GoTo loc_004024EB
  loc_004024B0: GoTo loc_004024DC
  loc_004024B2: 'Referenced from: 00402280
  loc_004024D3: var_eax = Unknown_VTable_Call[ecx+00000054h]
  loc_004024DA: If Unknown_VTable_Call[ecx+00000054h] >= 0 Then GoTo loc_004024EB
  loc_004024DC: 'Referenced from: 004024B0
  loc_004024E5: Unknown_VTable_Call[ecx+00000054h] = CheckObj(var_4C, var_00401B9C, 84)
  loc_004024EB: 'Referenced from: 004024AE
  loc_004024F4: GoTo loc_00402479
  loc_00402573: Exit Sub
  loc_00402574: 'Referenced from: 00402481
End Sub
